pipeline {
    agent any 
    environment {
        AWS_ECR_REPOSITORY_URL = "965220894814.dkr.ecr.us-east-1.amazonaws.com"
        WEB_APP_ECR_REPO_NAME = 'web-app'   
    }
    stages {
        stage ('Install Dependencies') {
            steps {
                script {
                    sh "pip install -r requirements.txt"
                }
            }
        }
        stage ('Dependency Scan') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'nvd-api-key', variable: 'NVD_API_KEY')]) {
                        dependencyCheck additionalArguments: "--scan ./ --nvdApiKey $NVD_API_KEY", odcInstallation: 'dependecy-tool'
                        dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
                        sh "ls -la"
                        
                    }
                }
            }
        }
        stage ('Sonar Analysis') {
            steps {
                script {
                    def SONAR_SCANNER_HOME =  tool name: 'sonar-scanner'
                    withSonarQubeEnv('sonar') {
                        sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=python-application"
                  }     
                }
            }
        }
        stage ('Publish zip file into nexus') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'nexus-creds', passwordVariable: 'NEXUS_PASSWORD', usernameVariable: 'NEXUS_USER_NAME')]) {
                         def DATE_TIME = sh(script: "date +%Y%m%d-%H%M%S", returnStdout: true).trim()
                         def arifactName = "python-web-application_${DATE_TIME}"
                         sh "zip -r python-web-application_${DATE_TIME}.zip ."
                         sh """
                         curl -u ${NEXUS_USER_NAME}:'${NEXUS_PASSWORD}' --upload-file python-web-application_${DATE_TIME}.zip  'http://54.235.29.9:8081/repository/python-application-repo/python-web-application_${DATE_TIME}.zip'
                         """
                   }

             }
          }
        }
    }
}
