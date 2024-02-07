import Adafruit_DHT
import sqlite3
import datetime
sensor = Adafruit_DHT.DHT11
pin = 4
HUMIDITY, TEMPERATURE = Adafruit_DHT.read_retry(sensor, pin)
query = """INSERT INTO DHT11 (DATETIME, TEMPERATURE, HUMIDITY) VALUES(?,?,?)"""
data = (datetime.datetime.now(), TEMPERATURE, HUMIDITY)
if HUMIDITY is not None and TEMPERATURE is not None:
    try:
        conn = sqlite3.connect('dht11.db')
        cur = conn.cursor()
        cur.execute(query, data)
        conn.commit()
    finally:
        conn.close()