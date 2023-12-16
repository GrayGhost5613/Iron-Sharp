from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
import sqlite3 
def get_db_connection():
    conn = sqlite3.connect('ironsharp.db')
    conn.row_factory = sqlite3.Row
    return conn
app = Flask(__name__)
@app.route("/")
def index():
    c = get_db_connection()
    products = c.execute('select * from products where  productid not in (1,2)').fetchall()
    return render_template('index.html',products=products,active_page='home')
@app.route("/about")
def about():
    return render_template("about.html",active_page='about')

@app.route("/login")
def login():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM user').fetchall()
    print(posts)
    #conn.close()
    return render_template('login.html', posts=posts,active_page='login')
@app.route("/cart")
def cart():
     return render_template('cart.html',active_page='cart')
if __name__ == "__main__":
    app.run(debug=True)
