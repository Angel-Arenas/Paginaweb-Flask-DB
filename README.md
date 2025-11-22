# Paginaweb-Flask-DB

Este proyecto utiliza una instancia **EC2-WEB** para ejecutar una aplicación Flask y una instancia **EC2-DB** para alojar la base de datos MySQL.  
La conexión se realiza mediante variables de entorno usando un archivo `.env` que **no debe subirse al repositorio**.

---

##  Arquitectura (EC2-WEB conectándose a EC2-DB)

1. La conexión desde la EC2-WEB se realiza mediante un archivo `.env` donde se configuran las variables de entorno de la base de datos.
2. En `app.py` se inicializa la conexión leyendo las variables del `.env` con python-dotenv.

---

##  Configuración de Grupos de Seguridad en AWS

### **Grupo de seguridad de la EC2-WEB**

1. Abrir el grupo de seguridad.
2. Agregar reglas de entrada:
   - **SSH (22/tcp)**
   - **HTTP (80/tcp)**
   - **HTTPS (443/tcp)**
   - **Se Habilita tambien el puerto 8000/tcp

### **Grupo de seguridad de la EC2-DB**

1. Abrir el grupo de seguridad.
2. Agregar reglas de entrada:
   - **SSH (22/tcp)**
   - **HTTP (80/tcp)** (opcional)
   - **HTTPS (443/tcp)** (opcional)
   - **MySQL/Aurora (3306/tcp)**  
     → Permitir únicamente desde la IP privada o el Security Group del servidor web.

---

##  Instalación y configuración de MySQL en la EC2-DB

### **Actualizar el sistema**
```bash
sudo apt update
sudo apt upgrade -y
Instalar MySQL
sudo apt install mysql-server -y

Ingresar como root del sistema
sudo su

(Opcional) Cambiar contraseña del usuario root del sistema
passwd root

Ingresar a MySQL
sudo mysql

(Opcional) Configurar contraseña de root de MySQL
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'TuContraseñaSegura';
FLUSH PRIVILEGES;

Salir
exit;

Ejecutar mysql_secure_installation
sudo mysql_secure_installation


Respuestas recomendadas:

Remove anonymous users: Yes

Disallow root login remotely: No

Remove test database: Yes

Reload privilege tables: Yes

Ingresar a MySQL nuevamente
mysql -u root -p

Crear usuario para la aplicación
CREATE USER 'angel'@'%' IDENTIFIED WITH mysql_native_password BY '123';
GRANT ALL PRIVILEGES ON *.* TO 'angel'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

Ver usuarios
SELECT User, Host FROM mysql.user;

Permitir conexiones remotas
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf


Cambiar:

bind-address = 127.0.0.1


por:

bind-address = 0.0.0.0


Guardar y salir.

Reiniciar MySQL
sudo systemctl restart mysql

Verificar estado
sudo systemctl status mysql

 Configuración del Security Group para MySQL en AWS

Abrir el puerto 3306

Permitir solo desde:

La IP privada de la EC2-WEB
o

El Security Group de la EC2-WEB

 Pasos para clonar el repositorio e iniciar la aplicación en EC2-WEB
1. Clonar el repositorio
git clone https://ENLACE_DEL_REPOSITORIO

2. Ver ramas
git branch

3. Cambiar a la rama principal del proyecto
git checkout develop


(o main, según tu caso)

4. Instalar dependencias del sistema
sudo apt install python3-pip python3-venv python3-dev nginx git -y

5. Crear entorno virtual
python3 -m venv venv

6. Activar entorno virtual
source venv/bin/activate

7. Instalar dependencias del proyecto
pip install -r requirements.txt

8. Ejecutar la aplicación con Gunicorn
gunicorn app:app --bind 0.0.0.0:8000
