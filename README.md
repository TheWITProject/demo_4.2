## Summary
You will be demoing how to a very simple API for our zoo app using `Flask-SQLAlchemy`. You can demonstrate changes to your database in psql, Postico/pgAdmin, or even the `GET` routes you write (although you might want to install [JSON Viewer](https://chrome.google.com/webstore/detail/json-viewer/aimiinbnnkboelefkjlenlgimcabobli).

## Installation
```
# in your postgres cluster, create a database named "zoo"
createdb zoo

# clone this repo
git clone <this repo's remote url>

# enter directory
cd demo_4.2

# create a virtual environment for this project & activate
mkdir env
python3 -m venv env
source env/bin/activate

# install the requirements
pip install -r requirements.txt

# create and seed tables
python app/db.py

# run application
python app/app.py
```

## Instructions

**Database & Models**

The focus of this lecture is using the `Flask` and `Flask-SQLAlchemy` API, so you shouldn't spend any time implementing or seeding database models. In fact, this has already been done for you in the installation steps above.

One thing you might want to cover is how we connect our database (see `app/app/py`, lines 5-8) and set up our models off of `db.Model` instead of the declarative base (see `app/models.py`, lines 3, 20, & 43). This syntax is slightly different from what fellows learned last week because we are using `Flask-SQLAlchemy` instead of just `SQLAlchemy`. You can share this [documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart) with the fellows to demonstrate this.

You should also point out that we need to define a `serialize` method in order to return data from our models as JSON. This too has already been done for you, but you should point out that the current solution is not the most scalable. There are packages that can help handle serialization, like `SQLAlchemy-serializer` and `marshmallow`, that we may want to use in the future.

**Demoing**

For the remainder of the lecture, focus on writing the API routes. When a route handles more than one method, write and demo each method one at a time before extending the route to handle an additional method. For example, `/animals` handles both `GET` and `POST` methods. Write and demo the `GET` route, then add control flow to handle the `POST` method.

You can check `app/solutions.py` for rough implementations of these, but remember that fellows should be doing most of the work during demos. If they need guidance, some helpful documentation to pull up for them include:
- [Flask-SQLAlchemy: Select, Insert, Delete](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/)
- [SQLAlchemy: Filter](https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.filter)
- [SQLAlchemy: Get](https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.get)
- [Flask: Quick Start, Variable Rules](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules)
- [Flask: Form Data](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request.form) *make sure to use the form tab on Postman to demo `POST`/`PUT` methods!
- [Flask: Quick Start, The Request Object](https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object) *has a form data example

**Extension**

Once you are done, talk about how the API you wrote can be improved. Is it easy to read? Is it resuable? `app/solutions.py` sure as heck isn't! For example, some of the database work can be extracted into helper methods so the routes are easier to read. Also, the routes don't send variable statuses relative to the actions nor do they handle any errors. You can work on fixing these things if there is time.
