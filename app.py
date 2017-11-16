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
            
    if not request.form['name']:
        flash('please enter book name')

    if not request.form['author']:
        flash('enter author name')

    if not request.form['price']:
        flash('enter book price')
    else:
                                  
        book=Book(name =request.form['name'],author=request.form['author'],price=request.form['price'])
        print 'book data ---',book
           
        db.session.add(book)
        db.session.commit()
        flash('Book Added Successfully')
    return book.name

@app.route('/update/<book_id>', methods=['PUT'])
def update(book_id):
    print 'book_id --',book_id
    if not request.form['name']:
        flash('enter book name')
    else:
        b= Book.query.get(book_id)
        print 'b ---',b
        b.name=request.form['name']
        b.author = request.form['author']
        b.price = request.form['price']
       
        db.session.commit()
    return b.name

@app.route('/remove/<book_id>', methods=['DELETE'])
def remove(book_id):
    print 'book_id--',book_id
    if not book_id:
        flash('book not found')
    else:
        b=Book.query.get(book_id)
        db.session.delete(b)
        db.session.commit()
    return b.name



if __name__ == '__main__':
    db.create_all()
    app.run()
