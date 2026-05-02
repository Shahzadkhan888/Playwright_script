pipeline {
agent any
stages {
       stage('Install Dependencies') {
            steps {
                echo " Installing Python dependencies"
                bat "pip install playwright pytest-playwright pytest-html"
                bat "playwright install chromium"
            }
        }
       stage('Run Playwright Tests'){
       steps{
             echo "Running Playwright Tests"
             bat "pytest testorgangehrm.py -v --html=report.html --junitxml=results.xml"



       }

       }
        stage('Publish Results') {
            steps {
                echo "📊 Publishing Test Results"
                junit 'results.xml'
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Playwright Test Report'
                ])
            }
        }
    }

      post {
        success {
            echo " All Playwright tests passed!"
        }
        failure {
            echo " Tests failed — check the Playwright report"
        }
    }
}



        }

        }

}

}