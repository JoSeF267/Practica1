Practica1
=========

 Práctica 1 - Infraestructura Virtual
=========================================

Para realizar esta práctica he decidido usar 'Heroku' porque la interfaz me parece bastante atractiva y porque simpatizo con las empresas pequeñas que acaban de empezar y parecen ofrecer buenos resultados. La aplicación que vamos a subir será en lenguaje **Python**.

Lo primero que debemos hacer para empezar a trabajar con nuestra aplicación en 'Heroku' es logearnos con el comando `heroku login`.

Acto seguido, creamos un directorio donde situar nuestra aplicación que va a usar Heroku mediante un framework llamado 'Flask'.

```
mkdir pythonProject
cd pythonProject/
```

Creamos un _Python virtualenv_ con

`virtualenv venv --distribute`

Lo activamos... `source venv/bin/activate`

Y ahora instalamos el _Flask framework_ y el servidor _gunicorn_ para poder trabajar con _python_ en 'Heroku':

` pip install Flask gunicorn`

y ahora ya tenemos todo listo para hacer nuestra aplicación en 'Python'.

En mi caso será un simple código en python que devuelve una página en HTML con alguna información y una imágen.

```
import os

from flask import Flask

app = Flask(__name__)

@app.route('/')       
def funcion():
	return "<html><title>Practica 1 IV</title><link type='text/css' rel='stylesheet' href='static/style.css'><body><center><h1>PRACTICA 1</h1><br><h2>INFRAESTRUCTURA VIRTUAL</h2><br></center><br><br>Esta es la primera practica de Fernando Llodra Belda para la asignatura de Infraestructura Virtual de 4o de Grado en Ingenieria Informatica.<br>Os dejo con una imagen curiosa<img_src='static/GameOfThrones_ColouredMap.jpg'></body></html>"
```


Una vez terminada, tenemos que crear un fichero 'Procfile' en nuestro directorio donde tenemos la aplicación Python e insertar la linea `web: gunicorn practica1IV:app`.


Iniciamos el proceso en nuestro Procfile con `foreman start`, vemos que todo está en orden y salimos con _Ctrl+C_.

Creamos en el directorio de nuestra aplicación un fichero llamado requirements.txt con `pip freeze > requirements.txt` y añadimos 
```
Flask==0.9
Jinja2==2.6
Werkzeug==0.8.3
gunicorn==0.17.2
```

Y ahora procedemos a alamcenar nuestra aplicación en git. Para ello iniciamos git y creamos un nuevo repositorio con:

```
git init
git add .
git commit -m "init"
```

Ahora añadimos nuestro repositorio a 'Heroku' `heroku create`. Con ésto creamos automaticamente el asistente remoto de heroku para nuestra aplicación.

Procedemos a 'pushear' nuestra aplicación (subirla) a heroku: `git push heroku master`

Ahora ya tenemos nuestra aplicación desplegada en Heroku. Ahora tenemos ejecutarla con Heroku. Para ello, Heroku usa un _'dyno'_.
Tenemos que asegurarnos de que hay algún 'dyno' para el proceso de ejecución web: `heroku ps:scale web=1
`
Lo tenemos, asique vemos el estado actual del 'dyno' y después visitamos nuestra app en nuestro navegador:

```
heroku ps
heroku open
```




