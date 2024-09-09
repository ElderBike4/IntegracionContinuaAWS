pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio
                git credentialsId: 'github-token', url: 'https://github.com/ElderBike4/IntegracionContinuaAWS.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                // Construir y levantar el servidor en Ubuntu
                sh 'docker build -t operaciones-app .'
                sh 'docker run -d -p 8081:80 operaciones-app'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv  # Crear el entorno virtual
                    . venv/bin/activate  # Activar el entorno virtual usando .
                    pip install selenium  # Instalar Selenium
                '''
            }
        }
        stage('Test') {
            steps {
                // Ejecutar las pruebas automatizadas en Ubuntu
                sh 'python3 ./tests/tests_operations.py'
            }
        }
        stage('Deploy') {
            when {
                expression { currentBuild.result == 'SUCCESS' }
            }
            steps {
                // Desplegar la aplicación (puede ser un servidor o contenedor)
                echo 'Desplegando la aplicación'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completado exitosamente.'
        }
        failure {
            echo 'El pipeline falló.'
        }
        always {
            script {
                sh './docker_commands.sh'
            }
        }
    }
}
