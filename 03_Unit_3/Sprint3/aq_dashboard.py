"""OpenAQ Air Quality Dashboard with Flask."""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq


APP = Flask(__name__)

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

DB = SQLAlchemy(APP)


def get_openaq_data():
    api = openaq.OpenAQ()
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    openaq_list = [(item['date']['utc'], item['value'])
                   for item in body['results']]
    return openaq_list


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '< Time {} -- Value {} >'.format(self.datetime, self.value)


@APP.route('/')
def root():

    data = str(Record.query.all())

    return data


@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    openaq_data = get_openaq_data()
    for i, values in enumerate(openaq_data):
        record = Record(id=i, datetime=values[0], value=values[1])
        DB.session.add(record)
        DB.session.commit()
    DB.session.close()
    return 'Data refreshed!'