pipeline {
    agent any

    stages {
        stage('Set up Python') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/python -m pip install -e ".[test]"'
            }
        }

        stage('Test') {
            steps {
                sh '.venv/bin/python -m pytest --junitxml=pytest.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'pytest.xml'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Build packages') {
            steps {
                sh '.venv/bin/python -m build'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'dist/*', fingerprint: true
        }
    }
}
