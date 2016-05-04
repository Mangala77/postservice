from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/api/v1.0/posts', methods=['GET'])
def get_posts():
    errors=[]
    try:
        r = requests.get('http://jsonplaceholder.typicode.com/posts')
        posts = r.json()
        json_post = jsonify({'posts': posts})
        return jsonify({'posts': posts}), 200
        #return render_template('posts.html', posts=posts)
    except:
        errors.append("Unable to get URL. Please make sure it's valid and try again")
        return render_template('posts.html', errors=errors)

@app.route('/api/v1.0/posts/<posts_id>', methods=['GET'])
def show_posts(posts_id):
     r_post = requests.get("http://jsonplaceholder.typicode.com/posts/%s" % posts_id)
     post = r_post.json()
     return jsonify({'post': post})

@app.route('/api/v1.0/posts/<posts_id>/comments', methods=['GET'])
def show_posts_comments(posts_id):
     r_comment = requests.get("http://jsonplaceholder.typicode.com/posts/%s/comments" % posts_id)
     comments = r_comment.json()
     return jsonify({'comments': comments})

@app.route('/api/v1.0/posts', methods=['POST'])
def create_posts(posts_id):
    data = {'postId': posts_id, 'name': 'test', 'email': 'test@field.com', 'body': 'test description'}
    headers = {'Content-Type': 'application/json'}
    r_comment = requests.post("http://jsonplaceholder.typicode.com/posts/%s/comments" % posts_id, data=json.dumps(data), headers=headers)
    comments = r_comment.json()
    return jsonify({'comments': comments})

if __name__ == '__main__':
  app.run(debug=True)
