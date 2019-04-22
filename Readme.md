# Python Avanzado
En este repositorio encuentras los ejemplos usados en el curso realizado en [https://escuela.it/](https://escuela.it/) 

## Clases
#### Clase 1
Principios de Clean code en Python
> Nota:  
> Ejemplos en [Jupyter](https://jupyter.org/)   

#### Clase 2
Colecciones en Python
#### Clase 3
Principios de programación funcional
#### Clase 4
Decoradores
#### Clase 5
Corutinas, AsyncIO, Metaclases
#### Clase 6 y 7
Ejemplo de librería para publicar en PyPI. Libreria implementa conceptos de Metaclases, Documentación (Sphinx), Pruebas

**Crear viertualenv**
```
python3 -m venv {your-envs-path}/exchange_escuela_it
source {your-envs-path}/exchange_escuela_it/bin/activate
```
**Para correr la documentación**
```
cd exchange-example
cd docs
make html
open _build/html/index.html
```
**Instalar la librería**
Esta librería está publicada en PyPI puedes instalarla usando
```
pip install exchange-escuela-it
```

#### Clase 8
Ejemplo projecto en Django y Flask

**Para correr proyecto en Django**:
```
python3 -m venv {your-envs-path}/escuela-it-django
cd escuela-it-django
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Para correr proyecto en Flask**:
```
python3 -m venv {your-envs-path}/escuela-it-flask
source {your-envs-path}/escuela-it-flask/bin/activate
cd escuela-it-flask
pip install -r requirements.txt
python app.py
python app_rest.py
python app_sqlite.py
```