from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://localhost/users_messages"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ihaveasecret'
modus = Modus(app)
db = SQLAlchemy(app)
toolbar = DebugToolbarExtension(app)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    image_url = db.Column(db.Text)
    messages = db.relationship(
        'Message', backref="user", lazy="dynamic", cascade="all,delete")


class Message(db.Model):

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


db.create_all()


@app.route('/')
def root():
    return redirect(url_for('users_index'))


@app.route('/users', methods=["GET"])
def users_index():
    """Show a page with info on all users"""
    return render_template('users/index.html', users=User.query.all())


@app.route('/users/new', methods=["GET"])
def users_new():
    """Show a form to create a new user"""
    return render_template('users/new.html')


@app.route("/users", methods=["POST"])
def users_create():
    """Handle form submission for creating a new user"""
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'])
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('users_index'))


@app.route('/users/<int:user_id>', methods=["GET"])
def users_show(user_id):
    """Show a page with info on a specific user"""
    found_user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=found_user)


@app.route('/users/<int:user_id>/edit', methods=["GET"])
def users_edit(user_id):
    """Show a form to edit an existing user"""
    found_user = User.query.get_or_404(user_id)
    return render_template('users/edit.html', user=found_user)


@app.route('/users/<int:user_id>', methods=["PATCH"])
def users_update(user_id):
    """Handle form submission for updating an existing user"""
    found_user = User.query.get(user_id)
    found_user.first_name = request.form['first_name']
    found_user.last_name = request.form['last_name']
    found_user.image_url = request.form['image_url']
    db.session.add(found_user)
    db.session.commit()
    return redirect(url_for('users_index'))


@app.route('/users/<int:user_id>', methods=["DELETE"])
def users_destroy(user_id):
    """Handle form submission for deleting an existing user"""
    found_user = User.query.get(user_id)
    db.session.delete(found_user)
    db.session.commit()
    return redirect(url_for('users_index'))


@app.route('/users/<int:user_id>/messages', methods=["GET"])
def messages_index(user_id):
    """Show a page with info on all messages for a specific user"""
    found_user = User.query.get(user_id)
    return render_template('messages/index.html', user=found_user)


@app.route('/users/<int:user_id>/messages/new', methods=["GET"])
def messages_new(user_id):
    """Show a form to create a new message for a specific user"""
    found_user = User.query.get(user_id)
    return render_template('messages/new.html', user=found_user)


@app.route('/users/<int:user_id>/messages', methods=["POST"])
def messages_create(user_id):
    """Handle form submission for creating a new message for a specific user"""
    new_message = Message(content=request.form['content'], user_id=user_id)
    db.session.add(new_message)
    db.session.commit()
    return redirect(url_for('messages_index', user_id=user_id))


@app.route('/messages/<int:message_id>', methods=["GET"])
def messages_show(message_id):
    """Show a page with info on a specific message"""
    found_message = Message.query.get_or_404(message_id)
    return render_template('messages/show.html', message=found_message)


@app.route('/messages/<int:message_id>/edit', methods=["GET"])
def messages_edit(message_id):
    """Show a form to edit an existing message"""
    found_message = Message.query.get_or_404(message_id)
    return render_template('messages/edit.html', message=found_message)


@app.route('/messages/<int:message_id>', methods=["PATCH"])
def messages_update(message_id):
    """Handle form submission for updating an existing message"""
    found_message = Message.query.get(message_id)
    found_message.content = request.form['content']
    user = found_message.user
    db.session.add(found_message)
    db.session.commit()
    return redirect(url_for('messages_index', user_id=user.id))


@app.route('/messages/<int:message_id>', methods=["DELETE"])
def messages_destroy(message_id):
    """Handle form submission for deleting an existing message"""
    found_message = Message.query.get(message_id)
    user = found_message.user
    db.session.delete(found_message)
    db.session.commit()
    return redirect(url_for('messages_index', user_id=user.id))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
