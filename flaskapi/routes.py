from flask import request, jsonify
from flaskapi import app, db
from flaskapi.models import User, BlogPost
from flaskapi import linked_list



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
    pass

@app.route("/user/<user_id>", methods = ["DELETE"])
def delete_user(user_id) :
    pass

@app.route("/blog_post/<user_id>", methods = ["POST"])
def create_blog_post(user_id) :
    pass

@app.route("/user/<user_id>", methods = ["GET"])
def get_all_blog_posts(user_id) :
    pass

@app.route("/blog_post/<blog_post_id>", methods = ["GET"])
def get_one_blog_post(blog_post_id) :
    pass

@app.route("/blog_post/<blog_post_id>", methods = ["DELETE"])
def delete_blog_post(blog_post_id) :
    pass