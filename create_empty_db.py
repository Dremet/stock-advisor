import sqlite3

con=sqlite3.connect('stock_prices.db')
cur=con.cursor()
cur.execute("CREATE TABLE stock_prices (id integer primary key, datetime text, stock text, price real)")
con.commit()
con.close()