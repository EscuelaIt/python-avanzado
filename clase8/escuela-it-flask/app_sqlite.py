from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(3), unique=True, nullable=False)
    country = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Currency %r>' % self.key


db.create_all()

usd = Currency(key='USD', country='United Stated')
eur = Currency(key='EUR', country='European Union')

db.session.add(usd)
db.session.add(eur)
db.session.commit()

api = Api(app)


class CurrenciesList(Resource):

    def get(self):
        currencies = Currency.query.all()
        return {currency.key: currency.country for currency in currencies}


api.add_resource(CurrenciesList, '/')

if __name__ == '__main__':
    app.run(debug=True)
