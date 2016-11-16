# ChatCube+
ChatCube+ will be the new revolutionary way to keep in contact with your classmates!

This repository will help us maintain the software while working on it from seperate
locations. Don't forget to sync changes after commiting to the master and always make
a brief description of the changes you've made.

To run ChatCube backend

git clone 
cd Chatcube
sudo easy_install pip (on MAC)
pip install django==1.9.2
pip install djangorestframework
pip install djangorestframework-jwt
./manage.py migrate
./manage.py runserver
go to localhost:8000/ in browser to see API
