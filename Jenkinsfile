pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Клонуємо репозиторій через SSH
                git branch: 'main', url: 'git@github.com:vitaliiklim/new_k8s_project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Встановлюємо залежності
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Запускаємо тести
                sh 'python -m unittest discover'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Створюємо Docker-образ
                sh 'docker build -t flask-server .'
            }
        }

        stage('Push to Local Registry') {
            steps {
                // Завантажуємо образ у локальний Docker реєстр
                sh '''
                docker tag flask-server localhost:5000/flask-server
                docker push localhost:5000/flask-server
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed!'
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
