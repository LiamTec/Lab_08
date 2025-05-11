## Lab 08n

# QuizMaster API

QuizMaster API es una API RESTful diseñada para gestionar cuestionarios, preguntas y respuestas. Permite a los usuarios interactuar con cuestionarios, realizar intentos y validar respuestas a través de varios puntos finales.

Requisitos
- Python 3.x
- Django 3.x o superior
- Django REST Framework
- Base de datos (SQLite, PostgreSQL, MySQL, etc.)

1. Clona el repositorio:
````
git clone https://github.com/LiamTec/Lab_08.git

cd quiz_api
````

2. Crea y activa un entorno virtual:
````
python -m venv venv

source venv/Scripts/activate 
````

3. Instala las dependencias:
````
pip install -r requirements.txt
````

4. Aplica las migraciones de la base de datos:
````
python manage.py migrate
````

5. Inicia el servidor de desarrollo:
````
python manage.py runserver
````

6. Accede a la API:
La API estará disponible en http://127.0.0.1:8000/api/.

Para los Profile (Perfil de usuario)
- GET /api/profile/id/: Recuperar un perfil específico.
- DELETE /api/profile/id/: Eliminar un perfil específico.
- PATCH /api/profile/update/id/: Actualizar parcialmente un perfil específico.

Para los QuizAttempt (Intentos de cuestionario)
- GET /api/quizattempt/id/: Recuperar un intento de cuestionario específico.
- DELETE /api/quizattempt/id/: Eliminar un intento de cuestionario específico.
- PATCH /api/quizattempt/update/id/: Actualizar parcialmente un intento de cuestionario específico.

Para los Category (Categorías)
- GET /api/category/id/: Recuperar una categoría específica.
- DELETE /api/category/id/: Eliminar una categoría específica.
- PATCH /api/category/update/id/: Actualizar parcialmente una categoría específica.

Para los Tag (Etiquetas)
- GET /api/tag/id/: Recuperar una etiqueta específica.
- DELETE /api/tag/id/: Eliminar una etiqueta específica.
- PATCH /api/tag/update/id/: Actualizar parcialmente una etiqueta específica.
- POST /api/tag/: Crear una nueva etiqueta.
- GET /api/tag/: Obtener la lista de todas las etiquetas.
- PUT /api/tag/id/: Actualizar una etiqueta específica.
  
Para los Quizzes (Cuestionarios)
- POST /api/quizzes/: Crear un nuevo cuestionario.
- GET /api/quizzes/: Obtener la lista de todos los cuestionarios.
- GET /api/quizzes/id/: Obtener un cuestionario específico.
- PUT /api/quizzes/id/: Actualizar un cuestionario específico.
- DELETE /api/quizzes/id/: Eliminar un cuestionario específico.
  
Para las Questions (Preguntas)
-POST /api/questions/: Crear una nueva pregunta.
- GET /api/questions/: Obtener la lista de todas las preguntas.
- GET /api/questions/id/: Obtener una pregunta específica.
- PUT /api/questions/id/: Actualizar una pregunta específica.
- DELETE /api/questions/id/: Eliminar una pregunta específica.
  
Para los Choices (Opciones de Respuesta)
- POST /api/choices/: Crear una nueva opción de respuesta.
- GET /api/choices/: Obtener la lista de todas las opciones de respuesta.
- GET /api/choices/id/: Obtener una opción de respuesta específica.
- PUT /api/choices/id/: Actualizar una opción de respuesta específica.
- DELETE /api/choices/id/: Eliminar una opción de respuesta específica.

Para los Users (Usuarios)
- POST /api/users/: Crear un nuevo usuario.
- GET /api/users/: Obtener la lista de todos los usuarios.
- GET /api/users/id/: Obtener un usuario específico.
- PUT /api/users/id/: Actualizar un usuario específico.
- DELETE /api/users/id/: Eliminar un usuario específico.
  
Métodos para validación de respuestas
- POST /api/quizzes/id/validate/: Validar las respuestas enviadas para un cuestionario específico.



