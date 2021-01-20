# API
## Set up local environment
- Make sure you have Python 3.6+ installed
- Create and activate your virtual environment
- Project comes with a sample sqlite db (with a couple of users added), you can use that or create a new one (username and pass for the sample db are admin/Pwd12345)
```
pip install -r requirements.txt
```
```
python manage.py migrate
```
This superuser creation step is not needed if you are using the provided sample db:
```
python manage.py createsuperuser --email admin@test.com --username admin
```
```
python manage.py collectstatic
```
```
python manage.py runserver 8888 
```


## Challenge

#### Functionality
This challenge consists of creating a Django REST API, which will support:
- listing pages
- retrieving page details
- retrieving page comments
- adding page comments
- replying to comments

The placeholder 'comments' and 'pages' apps are already created for you.

#### Requirements
- create django models for pages and comments
- each page has a title and description
- each page can contain between 0 an N comments
- comments can only have one parent comment (FB style, max depth=2)
- comments allow mentioning other users in the system
- comments contain a timestamp of creation
- comments contain information about the poster of the comment

You can create users and pages manually (in Django admin or by hand).
Comments must be created via the frontend client. 

#### Bonus points
- you receive **bonus points** for deploying the API to heroku (you may want to switch to using PostgreSQL db on Heroku)

# Challenge completion
Please upload your solution to your github and send us your repository URL.
If you deployed the API, please also send us the API URL.

 

