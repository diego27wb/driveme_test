Prueba Técnica para Backend Developer en DriveMe Barcelona
==========================================================

Bienvenido/a a la prueba técnica para el puesto de Backend Developer en DriveMe Barcelona. El objetivo de esta prueba es evaluar tus habilidades en la conexión a bases de datos desde distintos lenguajes, integración de APIs, realización de peticiones AJAX, y la aplicación de buenas prácticas de programación.

Tiempo estimado
---------------

30-45 minutos.

Objetivos
---------

*   Demostrar habilidad en la conexión a bases de datos.
*   Integrar APIs externas.
*   Realizar peticiones AJAX.
*   Aplicar buenas prácticas de programación.

Ejercicio Propuesto
-------------------

Deberás completar los archivos `index.php` y `app.py` para cumplir con las siguientes funcionalidades:

1.  Al cargar el archivo `index.php`, debe mostrar en el mapa todos los puntos almacenados en la base de datos. Al hacer clic sobre ellos, se mostrará información específica de cada punto.
2.  Al hacer clic en una parte del mapa sin marcadores, se debe realizar una petición AJAX a `/guardar-clima`, gestionada por Python (Flask) en el archivo `app.py`.
3.  Esta petición debe enviar la latitud y longitud, hacer una consulta a la API de OpenWeatherMap, guardar los datos recibidos en la base de datos y devolver una respuesta.

Puedes ver un ejemplo de la funcionalidad esperada en el siguiente gif:

![Demostración del proyecto](demostration.gif)

Instalación
-----------

### Preparación del entorno

1.  **Entorno virtual de Python:**
    
    *   Crea el entorno virtual: `python3 -m venv venv`
    *   Activa el entorno virtual:
        *   En Windows: `venv\Scripts\activate`
        *   En Linux/Mac: `source venv/bin/activate`
    *   Instala las dependencias: `pip install -r requirements.txt`
2.  **Configuración de la base de datos:**
    
    *   Modifica los datos en `config.ini` con los detalles de tu conexión a MySQL.
3.  **Inicialización de la base de datos:**
    
    *   Ejecuta `init-db.php` para crear la base de datos y la tabla `clima` con todas sus columnas.

### Ejecución

*   Si estás utilizando Flask para el endpoint de la API, debes ejecutar el archivo `app.py` y mantenerlo ejecutándose mientras desees que la ruta `/guardar-clima` esté operativa.


Extra
-----------
1. Crea un nuevo endpoint que reciba la latitud y longitud y te devuelva la media de los últimos 5 días de los valores que consideres relevantes (Temperatura, humedad, viento, ...) A parte de las condiciones máximas y mínimas.
(Para recibir datos de los últimos 5 días usa `http://api.openweathermap.org/data/2.5/forecast?lat=40.4&lon=-3.7&appid=fe18e4ee1578782f0e81d5783229a1fb&units=metric&lang=es`)

2. Usa alguna libreria para transformar las coordenadas en localidad y devuélvela en la respuesta.

3. Mediante los datos climatológicos de los últimos 5 días, haz una predicción del siguiente dato climatológico, usando el modelo predictivo que quieras, y devuelvelo en la llamada (dato climatológico y probabilidad).

A valorar
-----------

Se tendrá en cuenta cualquier mejora que se considere añadir

Aclaraciones
-----------

Este código es un punto de partida, puedes instalar las librerías que consideres y modificar, borrar o añadir todos los archivos que creas oportunos.

¡Mucho éxito!
-------------

Esperamos que disfrutes realizando esta prueba tanto como nosotros al diseñarla. ¡Ánimo y suerte!
