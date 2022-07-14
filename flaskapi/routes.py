from crypt import METHOD_BLOWFISH
from flask import request, jsonify
from flaskapi import app
from flaskapi.models import User, BlogPost



@app.route("/user", methods = ["POST"])
def create_user() :
    pass

@app.route("/user/descending_id", methods = ["GET"])
def get_all_users_descending() :
    pass

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