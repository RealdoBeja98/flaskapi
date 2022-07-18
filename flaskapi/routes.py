from flask import request, jsonify
from flaskapi import app, db
from . import models
from flaskapi.models import User, BlogPost
from flaskapi import linked_list
from . import hash_table




@app.route("/user", methods = ["POST"])
def create_user() :
    data = request.get_json()
    new_user = User(
        name = data["name"],
        email = data["email"],
        address = data["address"],
        phone = data["phone"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message" : "User created"}), 200

@app.route("/user/descending_id", methods = ["GET"])
def get_all_users_descending() :
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()

    for user in users:
        all_users_ll.insert_beginning(
            {
                "id" : user.id,
                "name" : user.name,
                "email" : user.email,
                "address" : user.address,
                "phone" : user.phone
            }
        )
    
    return jsonify(all_users_ll.to_list()), 200

@app.route("/user/ascending_id", methods = ["GET"])
def get_all_users_ascending() :
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()

    for user in users:
        all_users_ll.insert_at_end(
            {
                "id" : user.id,
                "name" : user.name,
                "email" : user.email,
                "address" : user.address,
                "phone" : user.phone
            }
        )
    
    return jsonify(all_users_ll.to_list()), 200

@app.route("/user/<int:user_id>", methods = ["GET"])
def get_one_user(user_id) :
    users = User.query.all()
    all_users_ll = linked_list.LinkedList()

    for user in users:
        all_users_ll.insert_beginning(
            {
                "id" : user.id,
                "name" : user.name,
                "email" : user.email,
                "address" : user.address,
                "phone" : user.phone
            }
        )
    user = all_users_ll.get_user_by_id(user_id)
    return jsonify(user), 200


@app.route("/user/<int:user_id>", methods = ["DELETE"])
def delete_user(user_id) :
    user = User.query.filter_by(id = user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({})



@app.route("/blog_post/<int:user_id>", methods = ["POST"])
def create_blog_post(user_id) :
    data = request.get_json()

    user = User.query.filter_by(id = user_id).first()
    if not user:
        return jsonify({"message": "user does not exist!"}), 400
    
    ht = hash_table.HashTable(10)

    ht.add_key_value("title", data["title"])
    ht.add_key_value("body", data["body"])
    ht.add_key_value("date", models.now)
    ht.add_key_value("user_id", user_id)

    new_blog_post = BlogPost(
        title = ht.get_value("title"),
        body = ht.get_value("body"),
        date = ht.get_value("date"),
        user_id = ht.get_value("user_id"),
    )
    db.session.add(new_blog_post)
    db.session.commit()
    return jsonify({"message" : "new blog post created"}), 200

@app.route("/user/<user_id>", methods = ["GET"])
def get_all_blog_posts(user_id) :
    pass

@app.route("/blog_post/<blog_post_id>", methods = ["GET"])
def get_one_blog_post(blog_post_id) :
    pass

@app.route("/blog_post/<blog_post_id>", methods = ["DELETE"])
def delete_blog_post(blog_post_id) :
    pass