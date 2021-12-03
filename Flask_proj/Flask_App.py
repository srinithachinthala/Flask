from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,g,request
import sqlite3

Flask_App1=Flask(__name__)

def connect_db():
    sql = sqlite3.connect('C:/Users/sc21241/Flask/food__log.db')
    return sql

#Checking sqlite3 available in global variable
def get_db():
    if not hasattr(g, 'sqlite3_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

#Close connection for every request
@Flask_App1.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@Flask_App1.route('/')
def hello_world():
    return render_template("home.html")

@Flask_App1.route('/add_food',methods=['GET', 'POST'])
def add_food():
    if request.method=="POST":
        name=request.form["food_name"]
        protien=int(request.form["Protein"])
        carbohydrates=int(request.form["carbohydrates"])
        fat=int(request.form["fat"])
        calaries=protien*4+carbohydrates*4+fat*4.

        db=get_db()
        db.execute('insert into food(name, protein, carbohydrates, fat, calories) values(?,?,?,?,?)',
        [name,protien,carbohydrates,fat,calaries])
        db.commit()
    return render_template("add_food.html")


@Flask_App1.route('/day')
def day():
    return render_template("day.html")

if __name__ == '__main__':
    Flask_App1.run(debug=True)
