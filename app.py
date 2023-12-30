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
@app.route("/search")
def search():
    query =request.args.get('query')
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products where title like ? and productid not in (1,2)  ',('%' + query + '%',)).fetchall()
    conn.close()
    return render_template('search_results.html', products=products,active_page='home')
def get_product_details(product_id):
    conn = get_db_connection()
    product=conn.execute('select * from products where productid = ?',(product_id,)).fetchone()
    conn.close()
    return product
@app.route("/cart")
def cart():
    cart_products = [get_product_details(product_id) for product_id in session.get('cart', [])]
    return render_template('cart.html', cart_products=cart_products, active_page='cart')
@app.route("/add_to_cart", methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    cart = session.get('cart', {})
    if isinstance(cart, dict):
        cart[product_id] = cart.get(product_id, 0) + 1
    else:
        cart = {product_id: 1}
    session['cart'] = cart
    flash('Product added to cart')
    return redirect(request.referrer)
@app.route('/increase_quantity', methods=['POST'])
def increase_quantity():
    product_id = str(request.form.get('product_id'))   
    print(f"Product ID: {product_id}")  
    cart = session.get('cart', {})
    print(f"Cart before: {cart}")  
    if isinstance(cart, dict):
        cart[product_id] = cart.get(product_id, 0) + 1
    else:
        cart = {product_id: 1}
    session['cart'] = cart
    session.modified = True  
    print(f"Cart after: {cart}")  
    return redirect(url_for('cart'))
@app.route('/decrease_quantity', methods=['POST'])
def decrease_quantity():
    product_id = str(request.form.get('product_id'))
    cart = session.get('cart', {})
    if isinstance(cart, dict):
        if cart.get(product_id, 0) > 1:
            cart[product_id] = cart.get(product_id) - 1 
        else:
            del cart[product_id]
    session['cart'] = cart
    session.modified = True 
    return redirect(request.referrer)
@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = request.form.get('product_id')
    cart = session.get('cart', {})
    if product_id in cart:
        del cart[product_id]
    session['cart'] = cart
    return redirect(request.referrer)
def calculate_subtotal(cart):
    subtotal = 0
    for product_id, quantity in cart.items():
        product = get_product_details(product_id)
        subtotal += product['price'] * quantity
    return subtotal
def calculate_tax(subtotal):
    tax_rate = 0.15
    return subtotal * tax_rate
@app.route('/checkout', methods=['GET','POST'])
def checkout():
    if request.method == 'POST':
        session['cart']={}
        flash("Thanks for your purchase!")
        return redirect(url_for('index'))
    else:
        cart_products = []
        cart= session.get('cart',{})
        for product_id, quantity in cart.items():
            product = dict(get_product_details(product_id))
            product['quantity'] = quantity  
            cart_products.append(product)
        subtotal = calculate_subtotal(cart)
        tax = calculate_tax(subtotal)
        total = subtotal + tax
        return render_template('checkout.html', cart =cart_products, subtotal =subtotal,tax =tax, total =total)
app.secret_key = 'Test'

if __name__ == "__main__":
    app.run(debug=True)
