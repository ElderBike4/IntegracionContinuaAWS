pipeline {
    agent any
    triggers {
        githubPush()
    }
    environment {
        PATH = "${env.PATH}:/home/ubuntu/.local/bin"
    }
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
                sh 'pipenv install selenium'
            }
        }
        stage('Test') {
            steps {
                // Ejecutar las pruebas automatizadas en Ubuntu
                sh 'pipenv run python3 ./tests/tests_operations.py'
            }
        }
        stage('Deploy') {
            when {
                expression { currentBuild.result == 'SUCCESS' }
            }
            steps {
                // Desplegar la aplicación
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
                sh 'chmod +x ./docker_commands.sh'

                sh './docker_commands.sh'
            }
        }
    }
}
