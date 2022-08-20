from flask import jsonify, make_response

# RESPONSE SUCCESS
def success(values, message):
    res = {
        'data' : values,
        'message': message,
    }

    return make_response(jsonify(res)), 200

# RESPONSE BAD REQUEST
def badRequest(values, message):
    res = {
        'data' : values,
        'message': message
    }

    return make_response(jsonify(res)), 400

# ARRAY TABLE POSTS
def array_posts(datas):
    values = []

    for data in datas:
        dict = {}
        dict['id'] = data[0]
        dict['title'] = data[1]
        dict['content'] = data[2]

        values.append(dict)

    return values

# SINGLE OBJECT TABLE POSTS
def obj_posts(data):

    dict = {}
    dict['id'] = data[0]
    dict['title'] = data[1]
    dict['content'] = data[2]

    return dict