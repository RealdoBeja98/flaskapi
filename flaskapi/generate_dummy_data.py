from flask import Flask
import pretty_errors
from random import randrange
from datetime import datetime
from faker import Faker

from flaskapi import app 
from flaskapi import db
from flaskapi.models import User, BlogPost




faker = Faker()

# create dummy users
for i in range(200):
    name = faker.name()
    address = faker.address()
    phone = faker.msisdn()
    email = f'{name.replace(" ", "_")}@email.com'
    new_user = User(name=name, address=address, phone=phone, email=email)
    db.session.add(new_user)
    db.session.commit()

# create dummy blog posts
for i in range(200):
    title = faker.sentence(5)
    body = faker.paragraph(190)
    date = faker.date_time()
    user_id = randrange(1, 200)

    new_blog_post = BlogPost(
        title=title, body=body, date=date, user_id=user_id
    )
    db.session.add(new_blog_post)
    db.session.commit()