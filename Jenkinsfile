pipeline {
    agent any 
    environment {
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
        // stage ('Dependecy scan') {
        //     steps {
        //         script {
        //             //sh "dependency-check --scan requirements.txt --out reports --format HTML"
        //             dependencyCheckAnalyzer outdir: 'reports',
        //                                 scanpath: '.',
        //                                 format: 'ALL'   // XML, HTML, JSON
        //             dependencyCheckPublisher pattern: 'reports/dependency-check-report.xml'
        //         }
        //     }
        // }
        stage ('sonar analysis') {
            steps {
                script {
                    def SONAR_SCANNER_HOME =  tool name: 'sonar-scanner'
                        sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner --version"
                        sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=python-application -Dsonar.login=sqa_ea508247dede6d75c3c69903082d722f2886b0a8 -Dsonar.host.url=http://54.235.29.9:9000"
                }
            }
        }
    }
}
