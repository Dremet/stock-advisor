import requests
import pandas
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime


def download_current_onvista_price(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, features="html.parser")
    price = soup.findAll("meta", {"property":"schema:price"})[0]['content']

    return price

def save_current_price_to_sqlite(cur, name, price):
    cur.execute(f"INSERT INTO stock_prices(datetime, stock, price) VALUES ('{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','{name}',{price})")

