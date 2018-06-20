from app import db


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


message_tag_table = db.Table('message_tags',
                             db.Column('message_id', db.Integer,
                                       db.ForeignKey('messages.id')),
                             db.Column('tag_id', db.Integer,
                                       db.ForeignKey('tags.id')))


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    messages = db.relationship(
        'Message',
        lazy="dynamic",
        secondary=message_tag_table,
        cascade="all,delete",
        backref=db.backref('tags', lazy="dynamic"))


db.create_all()