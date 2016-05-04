# postservice
web service in pythio which fetches posts and its related comment and create a comment for particular posts and unit testing using flask

1. Install Python (2.7x)
2. Install flask and import requests
3. posts.html is sample html which we can be view for response and for showing error as well
4. posts.py is the main script
5. posts_test is unit testing in Flask

To run the app.
1. Go to project folder and run python posts.py
2. hit the url 
  a. for getting all posts - http://127.0.0.1:5000/api/v1.0/posts
  b. for showing particular posts - http://127.0.0.1:5000/api/v1.0/posts/1
  c. for showing particular comments for posts - http://127.0.0.1:5000/api/v1.0/posts/1/comments
  d. for creating comments for particular posts - http://127.0.0.1:5000/api/v1.0/posts/1/comments
