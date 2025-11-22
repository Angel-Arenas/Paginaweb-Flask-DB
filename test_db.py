from dotenv import load_dotenv
import os
import mysql.connector
from mysql.connector import Error

load_dotenv()

try:
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DB')
    )
    
    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"✅ Conectado exitosamente a MySQL Server versión {db_info}")
        
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"✅ Base de datos actual: {record[0]}")
        
        cursor.close()
        connection.close()
        print("✅ Conexión cerrada correctamente")
        
except Error as e:
    print(f"❌ Error al conectar a MySQL: {e}")