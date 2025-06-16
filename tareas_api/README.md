# Tareas API

Este proyecto es una API REST básica para la gestión de tareas utilizando Django y Django REST Framework.

## Instalación

1. Clona el repositorio.
2. Crea un entorno virtual y actívalo.
3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Realiza migraciones:
   ```bash
   python manage.py migrate
   ```
5. Crea un superusuario:
   ```bash
   python manage.py createsuperuser
   ```
6. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```
7. Prueba la API en Postman o tu herramienta favorita en `http://localhost:8000/api/tareas/`.

## Estructura

- `tareas_api/`: Configuración del proyecto.
- `tareas/`: Aplicación con el modelo, serializador, vistas y rutas para las tareas.
