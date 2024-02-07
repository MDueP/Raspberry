import sqlite3
conn = sqlite3.connect('dht11.db') #Hvis den ikke eksistere, så laver den databasen 
#alt efter hvor python programmet er kørt fra
try:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE DHT11(
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        DATETIME TEXT NOT NULL, 
        TEMPERATURE REAL NOT NULL, 
        HUMIDITY REAL NOT NULL);""" )
        #cursor objektet skal altid gøre ting i string, da den ikke kan f.eks. sql
    conn.commit()
finally:
    conn.close()