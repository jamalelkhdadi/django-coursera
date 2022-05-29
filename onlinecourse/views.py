from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import BadHeaderError
from django.core import mail
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *

# for search name
from django.db.models import Q




def home(request):
    courses = Course.objects.all()

    context = {
        'courses': courses,
        'forms': forms,
    }

    return render(request, 'index.html', context)


def course(request):
    search = Course.objects.all()
    qestion = None
    if 'search_name' in request.GET:
        qestion = request.GET['search_name']
        if qestion:
            search = search.filter(
                Q(name__icontains=qestion) | Q(title__icontains=qestion) | Q(category__icontains=qestion)
            )
    context = {
        'courses': search,
    }
    return render(request, 'course/course.html', context)


class CourseListView(ListView):
    model = Course
    template_name = 'pages/home.html'
    context_object_name = 'courses'
    ordering = ['-date_posted']
    paginate_by = 3


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/course_form.html'
    success_url = reverse_lazy('course')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/course_detail.html'



class CourseUserListView(ListView):
    model = Course
    template_name = 'course/user_courses.html'
    context_object_name = 'courses'
    paginate_by = 4
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Course.objects.filter(author=user).order_by('-date_posted')

class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'course/course_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        course = self.get_object()
        if self.request.user == course.author:
            return True
        return False

class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    success_url = '/'
    template_name = 'course/course_confirm_delete.html'
    def test_func(self):
        course = self.get_object()
        if self.request.user == course.author:
            return True
        return False


# contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                connection = mail.get_connection()
                # Manually open the connection
                connection.open()
                # Construct an email message that uses the connection
                send_contact = mail.EmailMessage(subject, message, settings.EMAIL_HOST_USER, [
                    settings.EMAIL_RECIPIENT])
                send_contact.send()
                connection.close()
                messages.success(request, "Your Message received. thank You! ")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")
    form = ContactForm()
    return render(request, "pages/contact.html", {'form': form})



def about(request):
    return render(request, 'pages/about.html', {'title': 'About'})



def course_all(request):
    context = {
        'courses': Course.objects.all(),
        'title': 'course',
    }
    return render(request, 'course/course.html', context)



