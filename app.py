from flask import Flask, request
from response import *
from database import database
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = database()
cursor = db.cursor()

@app.route('/')
def index():
    return "index"

@app.route('/posts', methods=['GET','POST'])
def posts():
    if request.method == 'POST':

        title = request.form.get('title')
        content = request.form.get('content')

        input = [{
            'title': title,
            'content': content,
        }]

        sql = "INSERT INTO posts (title, content) VALUES (%s, %s)"
        val = (title, content)
        cursor.execute(sql, val)
        db.commit()
        return success(input, "success")

    else:

        sql = "SELECT * FROM posts"
        cursor.execute(sql)
        posts = cursor.fetchall()
        data = array_posts(posts)
        return success(data, "success")

@app.route('/post/<int:id>', methods=['GET','PATCH','DELETE'])
def post(id):
    if request.method == 'GET':

        try:
            sql = "SELECT * FROM posts WHERE id = " + str(id)
            cursor.execute(sql)
            posts = cursor.fetchone()
            data = obj_posts(posts)
            return success(data, "success")
        except:
            return badRequest([], 'Data Not Found')

    elif request.method == 'PATCH':

        title = request.form.get('title')
        content = request.form.get('content')

        input = [{
            'title': title,
            'content': content,
        }]

        sql = "UPDATE posts SET title = %s, content = %s WHERE id = %s"
        val = (title, content, id)
        cursor.execute(sql, val)
        db.commit()
        return success(input, "success")

    elif request.method == 'DELETE':

        sql = "DELETE FROM posts WHERE id = " + str(id)
        cursor.execute(sql)
        db.commit()
        return success('', 'Success Deleted')



if __name__ == '__main__':
    app.run(debug=True)