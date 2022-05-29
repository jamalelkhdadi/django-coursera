git add .
sleep 1
read commit
git commit -am "$commit"
sleep 1
git push -u origin main
sleep 1
git push heroku main
sleep 1
clear
git status