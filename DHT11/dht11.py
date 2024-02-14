import Adafruit_DHT
import sqlite3
import datetime
from time import sleep
from socket import *
sensor = Adafruit_DHT.DHT11
pin = 4
HUMIDITY, TEMPERATURE = Adafruit_DHT.read_retry(sensor, pin)
query = """INSERT INTO DHT11 (DATETIME, TEMPERATURE, HUMIDITY) VALUES(?,?,?)"""
serverSocket = socket(AF_INET, SOCK_DGRAM)
modtagerport = 12000
modtageraddr = ""
while HUMIDITY is not None and TEMPERATURE is not None:
    #Vigtigt de er inde i loopet, ellers bliver de ikke opdateret:
    HUMIDITY, TEMPERATURE = Adafruit_DHT.read_retry(sensor, pin)
    data = (datetime.datetime.now(), TEMPERATURE, HUMIDITY)
    try:
        conn = sqlite3.connect('dht11.db')
        cur = conn.cursor()
        cur.execute(query, data)
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print(f'Could not insert! {e}')
    finally:
        cur.execute("""SELECT * FROM DHT11 ORDER BY ID DESC LIMIT 20""") #limit fortæller at det er de første 20, med order by ID DESC, vender tabellen og de nyeste commits er nu i toppen
        dataudtræk=cur.fetchall()
        print(dataudtræk) #Det er ikke kønt, men det virker
        try:
            cur.execute("""SELECT * FROM DHT11 ORDER BY ID DESC LIMIT 1""")
            data_client=cur.fetchall()
            strdata_client = str(data_client)
            serverSocket.sendto(strdata_client.encode(), (modtageraddr, modtagerport))
        except Exception as error:
            print(f"Wifi Error '{error}', no connection")
            pass
        conn.close
        sleep(10)
