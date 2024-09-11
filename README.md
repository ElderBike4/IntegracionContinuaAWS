Instalación de jenkins en AWS EC2 Ubuntu


Actualizar paquetes
```bash
sudo apt-get update
```

Instalar JAVA JDK 17

```bash
sudo apt install openjdk-17-jre-headless
```

Instalar jenkins 

```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```
Visualizar el estado de jenkins
```sh
sudo systemctl status jenkins
```

Si jenkins no esta iniciado
```sh
sudo systemctl start jenkins
```

Recuperar la contraseña inicial de jenkins
```sh
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
Actualizar dependencias
```bash
sudo apt update
sudo apt upgrade
```

Paquetes necesarios para docker
```sh
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

Instalación de docker 

```bash

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update

sudo apt install docker-ce

sudo docker --version

```
Establecer docker para que se inicia al arrancar el sistema
```sh
sudo systemctl enable docker
```

Inicar docker si no esta iniciado
```sh
sudo systemctl start docker
```

instalar pip
```sh
sudo apt install python3-pip
```

Instalar pipenv
```sh
sudo pip install pipenv
```

Crear un token clasico en github y darle los permisos de repo, agregar este token a las credenciales globales de jenkins con el id `github-token`


Darle permisos a jenkins sobre docker
```sh
sudo chmod 666 /var/run/docker.sock
sudo usermod -aG docker jenkins
```

Reiniciar docker para que los cambios surtan efecto
```sh
sudo systemctl restart docker
```

Ejecutar `sudo visudo` y añadir el siguiente texto, para poder utilizar sudo en jenkins
```
jenkins ALL=(ALL) NOPASSWD: ALL
```

Chromedriver
```sh
wget https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.84/linux64/chromedriver-linux64.zip

unzip chromedriver-linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver

```

Chrome
```sh
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
google-chrome --version
```

Configurar Webhook en github con la url de jenkins agregando `/github-webhook/` y configurando el `content-type` en `application/json`