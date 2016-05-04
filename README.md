# postservice
web service in pythio which fetches posts and its related comment and create a comment for particular posts and unit testing using flask

1. Install Python (2.7x)
2. Install flask and import requests
3. posts.html is sample html which we can be view for response and for showing error as well
4. posts.py is the main script
5. posts_test is unit testing in Flask
6. Go to project folder and run python posts.py (to run the application)
7. for getting all posts - http://127.0.0.1:5000/api/v1.0/posts
8. for showing particular posts - http://127.0.0.1:5000/api/v1.0/posts/1
9. for showing particular comments for posts - http://127.0.0.1:5000/api/v1.0/posts/1/comments
10. for creating comments for particular posts - http://127.0.0.1:5000/api/v1.0/posts/1/comments
