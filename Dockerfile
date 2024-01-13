# Usa la imagen base de Python
FROM python:3

# Instalar libmysqlclient-dev
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# Establece el directorio de trabajo en /usr/src/app
WORKDIR /usr/src/app

# Copia los archivos de requisitos al contenedor
COPY requirements.txt ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del directorio actual al contenedor en /usr/src/app
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
