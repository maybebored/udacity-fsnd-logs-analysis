from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Product
from datetime import datetime, date

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalog.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/login', methods=['GET', 'POST'])
def showLogin():
    return render_template('login.html')

@app.route('/')
@app.route('/home/') #home page
def catalogMain():
    products_query = session.query(Product).filter(Product.created_on > date(2019,1,1))
    categories_query = session.query(Product.category.distinct().label("category"))
    # products = [row.category for row in categories_query.all()]
    categories = [ row.category for row in categories_query.all()]
    return render_template('home.html',products=products_query,categories=categories)

@app.route('/catalog/<string:category>/') #category page
def getProductsByCategory(category):
    categories_query = session.query(Product.category.distinct().label("category"))
    categories = [ row.category for row in categories_query.all()]
    products_query = session.query(Product).filter(Product.category == category)
    return render_template('category.html',products=products_query,categories=categories)

@app.route('/catalog/product/<int:product_id>/')
def getProduct(product_id):
    products_query = session.query(Product).filter(Product.id == product_id).one()
    return render_template('product.html',product=products_query)


# JSON APIs for Product Catalog App
# GET all items
@app.route('/api/catalog/', methods=['GET'])
def catalogJSON():
    products = session.query(Product).all()
    return jsonify(catalog=[(p.title,p.description) for p in products]);

# GET all categories
@app.route('/api/catalog/categories/', methods=['GET'])
def categoriesJSON():
    products = session.query(Product.category.distinct().label('category'))
    return jsonify(categories = [p.category for p in products])



if __name__ == '__main__':
    # app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)