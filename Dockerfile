# Usa una imagen base de Nginx
FROM nginx:alpine

# Copia el contenido de la carpeta 'src' a la carpeta predeterminada de Nginx
COPY ./src/web /usr/share/nginx/html

# Expone el puerto 80
EXPOSE 80

# Ejecuta el servidor Nginx en primer plano
CMD ["nginx", "-g", "daemon off;"]
