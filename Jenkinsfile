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
                        pip install -r requirements.txt  // Install dependencies
                    '''
                }
            }
        }

        stage('Train Model') {
            steps {
                script {
                    // Activate the virtual environment and run the training script
                    sh '''
                        . venv/bin/activate
                        python3 train.py  // Run the training script directly (since it's in the root folder)
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker tag $DOCKER_IMAGE $DOCKER_HUB_REPO:latest'
                    sh 'docker push $DOCKER_HUB_REPO:latest'
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
