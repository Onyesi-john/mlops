pipeline {
    agent any

    environment {
    DOCKER_IMAGE = 'latest'
    GITHUB_REGISTRY = 'ghcr.io'  // GitHub Container Registry
    GITHUB_REPO = 'onyesi-john/mlops'  // Replace with your actual GitHub repository name
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

        stage('Build Docker Image') {
             steps {
                  script {
                           // Authenticate to GitHub Container Registry using Jenkins credentials
                          withDockerRegistry([credentialsId: 'new_pipeline', url: "https://${GITHUB_REGISTRY}"]) {
                          // Build the Docker image with the correct tag format
                       sh 'docker build -t ${GITHUB_REGISTRY}/${GITHUB_REPO}:${DOCKER_IMAGE} .'
                  }
              }
           }
       }


        stage('Push to GitHub Container Registry') {
            steps {
                script {
                    // Push the Docker image to GitHub Container Registry
                    withDockerRegistry([credentialsId: 'new_pipeline', url: "https://${GITHUB_REGISTRY}"]) {
                        sh 'docker push ${GITHUB_REGISTRY}/${GITHUB_REPO}:${DOCKER_IMAGE}'
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
