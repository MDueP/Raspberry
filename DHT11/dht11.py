import Adafruit_DHT
import sqlite3
import datetime
from time import sleep
sensor = Adafruit_DHT.DHT11
pin = 4
HUMIDITY, TEMPERATURE = Adafruit_DHT.read_retry(sensor, pin)
query = """INSERT INTO DHT11 (DATETIME, TEMPERATURE, HUMIDITY) VALUES(?,?,?)"""
while HUMIDITY is not None and TEMPERATURE is not None:
    #Vigtigt den er inde i loopet, ellers bliver tiden ikke opdateret:
    data = (datetime.datetime.now(), TEMPERATURE, HUMIDITY)
    try:
        conn = sqlite3.connect('dht11.db')
        cur = conn.cursor()
        cur.execute(query, data)
        conn.commit()
    finally:
        cur.execute("""SELECT * FROM DHT11 ORDER BY ID DESC LIMIT 20""") #limit fortæller at det er de første 20, med order by ID DESC, vender tabellen og de nyeste commits er nu i toppen
        dataudtræk=cur.fetchall()
        print(dataudtræk) #Det er ikke kønt, men det virker
        conn.close
        sleep(10)