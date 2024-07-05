from flask import Flask, request, render_template
import sqlite3

con = sqlite3.connect("athletes.db")
cur = con.cursor()
res = cur.execute("SELECT * From Athletes")
sportsmens = res.fetchall()

print (sportsmens)

#Добавление новой записи. 

con = sqlite3.connect("athletes.db")
new_sportsmen = "INSERT INTO Athletes(Name,Gender,Age,Country,Sport) VALUES ('Юрий', 'M', 26 , 'Сербия', 'Плавание')";
cur = con.cursor()
cur.execute(new_sportsmen)
con.commit()
cur.close()
con.close()









