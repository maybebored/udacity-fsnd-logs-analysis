from flask import Flask, jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Product

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalog.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def catalogMain():
    products = session.query(Product).order_by(asc(Product.category))
    output = '<ul>'
    for product in products:
        output += '<li>'+product.title+'</li>'
    output += '</ul>'
    return output

# JSON APIs to get all products
@app.route('/api/catalog/JSON', methods=['GET'])
def catalogJSON():
    product = session.query(Product).one()
    return product.title;

@app.route('/catalog/<string:category>/<int:product_id>/')
def getProduct(category,product_id):
    # product = session.query(Product).filter_by(id=product_id).one()
    return 

if __name__ == '__main__':
    # app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)