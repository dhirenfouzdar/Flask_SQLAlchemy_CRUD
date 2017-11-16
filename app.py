from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, request, flash
import psycopg2 



app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "random string"
# POSTGRES = {
#     'user': 'postgres',
#     'pwd':'postgres',
#     'db': 'bookdb',
#     'host': 'localhost',
#     'port': '5432',
# }


db = SQLAlchemy(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/bookdb'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pwd)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    price = db.Column(db.Integer)

# def __init__(self, *args):
#         super().__init__(*args)

def __init__(self,name,author,price):
    # self.id=data.get('id',None)
    self.name = name
    self.author = author
    self.price = price
    
    
@app.route('/')
def main():
    return 'Hello world'

@app.route('/create_book', methods=['POST'])
def create():
    print ' bb'
    if request.method=='POST':
        print 'postin else '
        print 'inside create method'
        if not request.form['name']:
            flash('please enter book name')

        if not request.form['author']:
            flash('enter author name')

        if not request.form['price']:
            flash('enter book price')
        else:
            print 'inside else '
            # name = request.form['name']
            # author = request.form['author']
            # price = request.form['price']
            
            book=Book(name =request.form['name'],author=request.form['author'],price=request.form['price'])
            print 'book data ---',book
           
            db.session.add(book)
            db.session.commit()
            flash('Book Added Successfully')
    return book.name


if __name__ == '__main__':
    db.create_all()
    app.run()
