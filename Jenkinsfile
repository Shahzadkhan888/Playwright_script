pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies'
                bat 'C:\\Users\\shahz\\AppData\\Local\\Python\\bin\\python.exe -m pip install playwright pytest-playwright pytest-html'
                bat 'C:\\Users\\shahz\\AppData\\Local\\Python\\bin\\python.exe -m playwright install chromium'
            }
        }
        stage('Run Playwright Tests') {
            steps {
                echo 'Running Playwright Tests'
                bat 'C:\\Users\\shahz\\AppData\\Local\\Python\\bin\\python.exe -m pytest testorgangehrm.py -v --junitxml=results.xml'
            }
        }
        stage('Publish Results') {
            steps {
                junit 'results.xml'
            }
        }
    }
    post {
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}