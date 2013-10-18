import os

from flask import Flask

app = Flask(__name__)

@app.route('/')       
def funcion():
	return "<html><title>Practica 1 IV</title><link type='text/css' rel='stylesheet' href='static/style.css'><body><center><h1>PRACTICA 1</h1><br><h2>INFRAESTRUCTURA VIRTUAL</h2><br></center><br><br>Esta es la primera practica de Fernando Llodra Belda para la asignatura de Infraestructura Virtual de 4o de Grado en Ingenieria Informatica.<br>Os dejo con una imagen curiosa<img src='static/GameOfThrones_ColouredMap.jpg'></body></html>"
