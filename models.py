# models.py
import sqlite3

def create_tables():
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()

    # Create table for seasonal flavors
    c.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            available BOOLEAN NOT NULL
        )
    ''')

    # Create table for ingredient inventory
    c.execute('''
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    # Create table for customer suggestions and allergies
    c.execute('''
        CREATE TABLE IF NOT EXISTS customer_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_name TEXT NOT NULL,
            allergens TEXT
        )
    ''')

    # Insert initial data for seasonal flavors
    c.execute('''
        INSERT INTO seasonal_flavors (name, description, available) VALUES
        ('Vanilla Bean', 'Classic vanilla with a hint of real vanilla beans', 1),
        ('Strawberry Swirl', 'Fresh strawberries with a swirl of strawberry sauce', 1),
        ('Chocolate Fudge', 'Rich chocolate with fudge chunks', 0)
    ''')

    conn.commit()
    conn.close()

create_tables()
