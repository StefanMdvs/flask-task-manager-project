import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
"""
Since we are not going to push the env.py file to GitHub, once our app is deployed to
Heroku, it won't be able to find the env.py file, so it will throw an error.
This is why we need to only import env if the os can find an existing file path for
the env.py file itself.
"""
if os.path.exists("env.py"):
    import env


# create an instance of Flask
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = mongo.db.tasks.find()
    return render_template("tasks.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # don't forget to set debug to false before heroku
            debug=True)
