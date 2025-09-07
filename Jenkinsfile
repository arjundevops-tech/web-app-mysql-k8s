pipeline {
    agent any 
    environments {
        AWS_ECR_REPOSITORY_URL = "965220894814.dkr.ecr.us-east-1.amazonaws.com"
        WEB_APP_ECR_REPO_NAME = 'web-app'   
    }
    stages {
        stage ('install dependencies') {
            steps {
                script {
                    sh "pip install -r requirements.txt"
                }
            }
        }
        stage ('Dependecy scan') {
            steps {
                script {
                    sh "dependency-check --scan requirements.txt --out reports --format HTML"
                }
            }
        }
        stage ('sonar analysis') {
            steps {
                script {
                    def SONAR_SCANNER_HOME =  tool name: 'sonar-scanner'
                    withSonarQubeEnv('sonar'){
                        sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner --version"
                        sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner -Dsonar.projecKey=python-application"
                    }
                }
            }
        }
    }
