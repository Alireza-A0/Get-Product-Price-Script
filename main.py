# product_price_tracker.py

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import sqlite3
import datetime
import logging

logging.basicConfig(filename='price_tracker.log', level=logging.INFO)

def get_product_price(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        price_td = soup.find('td', class_='price')
        a_element = price_td.find('a')

        if a_element:
            product_price = a_element.text.strip()
            price = int(product_price.replace(',', ''))
            return price
        else:
            return None
    except Exception as e:
        logging.error(f"Error in get_product_price: {str(e)}")
        return None

def send_email(subject, body, to_email):
    sender = "Private Person <from@example.com>"
    receiver = "A Test User <toEmail@gmail.com>"

    message = MIMEText(body, 'html')
    message['Subject'] = subject
    message['To'] = receiver
    message['From'] = sender

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.login("741e0*******", "cd9*********")
        server.sendmail(sender, receiver, message.as_string())

def track_price():
    product_url = 'https://www.mobile.ir/phones/prices.aspx?terms=&brandid=7&provinceid=&duration=7&price_from=-1&price_to=-1&shopid=&pagesize=50&sort=date&dir=desc&submit=%D8%AC%D8%B3%D8%AA%D8%AC%D9%88'
    to_email = 'recipient@example.com'  # Replace with the recipient's email
    db_file = 'price_tracker.db'

    try:
        # Connect to SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prices (
                date TEXT,
                price TEXT
            )
        ''')

        # Get current date and price
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        current_price = get_product_price(product_url)

        # Retrieve the previous price from the database
        cursor.execute('SELECT price FROM prices ORDER BY date DESC LIMIT 1')
        previous_price = cursor.fetchone()

        if previous_price:
            previous_price = previous_price[0]

            # Compare current price with the previous price
            if current_price and current_price != previous_price:
                # Save current price to the database
                cursor.execute('INSERT INTO prices (date, price) VALUES (?, ?)', (current_date, current_price))
                conn.commit()

                # Send email notification
                subject = 'Price Change Alert!'
                body = f'The price has changed.<br><br>Previous Price: {previous_price}<br>Current Price: {current_price}<br>Product URL: {product_url}'
                send_email(subject, body, to_email)

        else:
            # If no previous price exists, save the current price to the database
            if current_price:
                cursor.execute('INSERT INTO prices (date, price) VALUES (?, ?)', (current_date, current_price))
                conn.commit()

    except Exception as e:
        logging.error(f"Error in track_price: {str(e)}")

    finally:
        # Close the database connection
        if conn:
            conn.close()

if __name__ == '__main__':
    track_price()
