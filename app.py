from flask import Flask, request, render_template, redirect, url_for
from database import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    flavors = conn.execute('SELECT * FROM seasonal_flavors').fetchall()
    conn.close()
    return render_template('index.html', flavors=flavors)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        conn = get_db_connection()
        flavors = conn.execute('SELECT * FROM seasonal_flavors WHERE name LIKE ?', ('%' + search_term + '%',)).fetchall()
        conn.close()
        return render_template('search.html', flavors=flavors)
    return render_template('search.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/add_allergen', methods=['POST'])
def add_allergen():
    flavor_name = request.form['flavor_name']
    allergen = request.form['allergen']
    conn = get_db_connection()
    conn.execute('INSERT INTO customer_suggestions (flavor_name, allergens) VALUES (?, ?)', (flavor_name, allergen))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
