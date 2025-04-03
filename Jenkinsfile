pipeline {
    agent {
        label (env.JOB_NAME.contains('dev') ? 'Dev' : 'Prod')
    }

    environment {
        BRANCH_NAME = 'default'   // temporary
        IMAGE_TAG = 'default'     // temporary
    }

    stages {
        stage('Set Environment Variables') {
            steps {
                script {
                    env.BRANCH_NAME = env.JOB_NAME.contains('dev') ? 'dev' : 'master'
                    env.IMAGE_TAG = env.JOB_NAME.contains('dev') ? 'latest-dev' : 'latest-prod'
                    echo "Branch to be cloned: ${env.BRANCH_NAME}"
                }
            }
        }

        stage('Checkout Code') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: "*/${env.BRANCH_NAME}"]],
                    userRemoteConfigs: [[url: 'https://github.com/MehulPanchal23/flaskappproject.git']]
                ])
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t flaskappproject:${env.IMAGE_TAG} ."
            }
        }

        stage('Push Image to Docker HUB') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "dockerhubcred",
                    passwordVariable: "dockerhubpass",
                    usernameVariable: "dockerhubuser"
                )]) {
                    sh "docker login -u ${env.dockerhubuser} -p ${env.dockerhubpass}"
                    sh "docker tag flaskappproject:${env.IMAGE_TAG} ${env.dockerhubuser}/flaskappproject:${env.IMAGE_TAG}"
                    sh "docker push ${env.dockerhubuser}/flaskappproject:${env.IMAGE_TAG}"
                }
            }
        }

        stage('Deploy on Server') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'master') {
                        echo "Deploying Production Image"
                        sh "docker pull ${env.dockerhubuser}/flaskappproject:latest-prod"
                        sh "docker tag ${env.dockerhubuser}/flaskappproject:latest-prod flaskappproject:prod"
                        sh "docker compose up -d"
                    } else {
                        echo "Deploying Dev Image"
                        sh "docker compose up -d"
                    }
                }
            }
        }
    }

    post {
        success {
            emailext from: "panchalmehul191@gmail.com",
                     subject: "Build Successful: ${env.BRANCH_NAME}",
                     body: "Build and Deployment Successful for ${env.BRANCH_NAME}",
                     to: "panchalmehul195@gmail.com"
        }
        failure {
            emailext from: "panchalmehul191@gmail.com",
                     subject: "Build Failed: ${env.BRANCH_NAME}",
                     body: "Check Logs for Errors in ${env.BRANCH_NAME}",
                     to: "panchalmehul195@gmail.com"
        }
    }
}
