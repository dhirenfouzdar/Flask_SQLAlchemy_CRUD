from flask_sqlalchemy import SQLAlchemy 
from flask import Flask 



app = FLASK(__name__)

app.config['DEBUG'] = True
POSTGRES = {
    'user': 'postgres',
    'password': 'postgres',
    'db': 'bookdb',
    'host': 'localhost',
    'port': '3000',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(password)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy()

@app.route('/')
def main():
    return 'Hello World!'

if __name = '__main__':
   
    app.run()
