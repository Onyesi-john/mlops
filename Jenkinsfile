pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-dl-model:latest'
        DOCKER_HUB_REPO = 'mydockerhubuser/my-dl-model'
    }

    stages {
        stage('Clone Repository') {
            steps {
               git branch: 'main', url: 'https://github.com/Onyesi-john/mlops.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                script {
                    // Set up the virtual environment and install dependencies
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt 
                    '''
                }
            }
        }

        stage('Train Model') {
            steps {
                 script {
                       sh '''#!/bin/bash
                       source venv/bin/activate
                      python train.py
                     '''
                   }
               }
            }


        stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Authenticate to Docker Hub using the stored credentials
                    withDockerRegistry([credentialsId: 'oyinc-docker']) {
                        sh 'docker build -t ${IMAGE_NAME} .'
                    }
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    // Authenticate again and push the image to Docker Hub
                    withDockerRegistry([credentialsId: 'oyinc-docker']) {
                        sh 'docker push ${IMAGE_NAME}'
                    }
                }
            }
        }

        stage('Monitor Model Performance') {
            steps {
                sh 'curl http://localhost:9090/api/v1/query?query=loss'
            }
        }

        stage('Trigger Auto-Retraining') {
            steps {
                script {
                    def loss = sh(script: "python check_loss.py", returnStdout: true).trim()
                    if (loss.toDouble() > 0.5) {
                        sh 'python3 retrain.py'
                    }
                }
            }
        }
    }
}
