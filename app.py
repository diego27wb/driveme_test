from flask import Flask, request, jsonify
import requests
import pymysql
from datetime import datetime
from flask_cors import CORS
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
CORS(app)


# Función para conectarse a la base de datos
def connect_db():
	#Conectate a la DB!
    host = config['default']['host']
    user = config['default']['username']
    password = config['default']['password']
    dbname = config['default']['db_name']
    
    # Conexión a la base de datos
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=dbname
    )
    return conn

@app.route('/clima-media', methods=['POST'])
def clima_media():
    # Obtener latitud y longitud de los datos enviados en la petición
    lat = request.form.get('lat')
    lon = request.form.get('lon')
    
    # Construir la URL para obtener los datos climáticos de los últimos 5 días
    api_key = config['default']['api-key']
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=es"

    # Realizar la petición a la API de OpenWeatherMap
    response = requests.get(url)
    data = response.json()

    # Extraer los datos climáticos relevantes de los últimos 5 días
    relevant_data = data['list'][-5:]  # Tomar los últimos 5 días
    temperatura = [dato['main']['temp'] for dato in relevant_data]
    humedad = [dato['main']['humidity'] for dato in relevant_data]
    viento = [dato['wind']['speed'] for dato in relevant_data]

    # Calcular las medias de temperatura, humedad y velocidad del viento
    media_temperatura = sum(temperatura) / len(temperatura)
    media_humedad = sum(humedad) / len(humedad)
    media_viento = sum(viento) / len(viento)

    # Calcular las condiciones máximas y mínimas
    max_temperatura = max(temperatura)
    min_temperatura = min(temperatura)
    max_humedad = max(humedad)
    min_humedad = min(humedad)
    max_viento = max(viento)
    min_viento = min(viento)

    # Devolver la respuesta JSON con los resultados
    return jsonify({
        "media_temperatura": media_temperatura,
        "media_humedad": media_humedad,
        "media_viento": media_viento,
        "max_temperatura": max_temperatura,
        "min_temperatura": min_temperatura,
        "max_humedad": max_humedad,
        "min_humedad": min_humedad,
        "max_viento": max_viento,
        "min_viento": min_viento
    })

@app.route('/guardar-clima', methods=['POST'])
def guardar_clima():
	# Obtener lat y lon de los datos enviados en la petición
	lat = request.form.get('lat')
	lon = request.form.get('lon')
	fecha = datetime.now().strftime('%Y-%m-%d')  # Fecha actual para el ejemplo
	# Realizar la petición a la API de clima
	api_key = config['default']['api-key']
	url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=es"
	
	#Realizamos petición, guardamos datos, y devolvemos json
	#Realizamos peticion de la API
	response = request.get(url)
	data = response.json()

	#Extraer datos relevantes de la respuesta
	temperatura = data['main']['temp']
	humedad = data['main']['humidity']
	viento = data['wind']['speed']
	descripcion = data['weather'][0]['description']

	#Guardar datos en la base de datos
	conn = connect_db()
	cursor = conn.cursor()
	sql = "INSERT INTO clima (fecha, lat, lon, temperatura, humedad, viento, descripcion, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
	values = (fecha, lat, lon, temperatura, humedad, viento, descripcion, url)
	cursor.execute(sql, values)
	conn.commit()
	conn.close()

	#Devolver respuesta JSON
	return jsonify({"success": True, "message": "Datos del clima guardados correctamente.", "fecha": fecha, "temperatura" : 0, "humedad" : 0, "viento" : 0, "descripcion" : 0, "url" : url})

if __name__ == '__main__':
	app.run(debug=True)
