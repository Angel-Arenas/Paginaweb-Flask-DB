from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Función para obtener conexión a la base de datos
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DB')
        )
        return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    telefono = request.form.get('telefono', '')
    
    if not nombre or not email:
        flash('Por favor completa todos los campos obligatorios', 'error')
        return redirect(url_for('index'))
    
    connection = get_db_connection()
    if connection is None:
        flash('Error de conexión a la base de datos', 'error')
        return redirect(url_for('index'))
    
    try:
        cursor = connection.cursor()
        query = "INSERT INTO contactos (nombre, email, telefono, fecha_registro) VALUES (%s, %s, %s, %s)"
        values = (nombre, email, telefono, datetime.now())
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        flash('¡Contacto registrado exitosamente!', 'success')
    except Error as e:
        print(f"Error al guardar: {e}")
        flash('Error al guardar el contacto', 'error')
        if connection:
            connection.close()
    
    return redirect(url_for('index'))

@app.route('/lista')
def lista():
    connection = get_db_connection()
    if connection is None:
        flash('Error de conexión a la base de datos', 'error')
        return redirect(url_for('index'))
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contactos ORDER BY fecha_registro DESC")
        contactos = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('lista.html', contactos=contactos)
    except Error as e:
        print(f"Error al cargar contactos: {e}")
        flash('Error al cargar los contactos', 'error')
        if connection:
            connection.close()
        return redirect(url_for('index'))

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False') == 'True'
    app.run(debug=debug_mode)