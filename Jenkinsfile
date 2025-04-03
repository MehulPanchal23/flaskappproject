pipeline {
    agent { 
        label (env.JOB_NAME.contains('dev') ? 'Dev' : 'prod') // Select agent dynamically
    }
    stages {
        stage("Initialize Variables") {
            steps {
                script {
                    env.BRANCH_NAME = env.JOB_NAME.contains('dev') ? 'dev' : 'master'
                    env.IMAGE_TAG = env.JOB_NAME.contains('dev') ? 'latest-dev' : 'latest-prod'
                }
            }
        }
        stage("Code Clone from GitHub") {
            when { expression { env.JOB_NAME.contains('dev') } } // Only for Dev pipeline
            steps {
                script {
                    echo "Cloning branch: ${env.BRANCH_NAME}"
                    git url: "https://github.com/MehulPanchal23/flaskappproject.git", branch: env.BRANCH_NAME
                }
            }
        }
        stage("Build Docker Image") {
            when { expression { env.JOB_NAME.contains('dev') } } // Only for Dev pipeline
            steps {
                sh "docker build -t flaskappproject:${env.IMAGE_TAG} ."
            }
        }
        stage("Push Image to Docker HUB") {
            when { expression { env.JOB_NAME.contains('dev') } } // Only for Dev pipeline
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
        stage("Re-tag and Push Prod Image") {
            when { expression { env.JOB_NAME.contains('prod') } } // Only for Prod pipeline
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "dockerhubcred",
                    passwordVariable: "dockerhubpass",
                    usernameVariable: "dockerhubuser"
                )]) {
                    sh "docker login -u ${env.dockerhubuser} -p ${env.dockerhubpass}"
                    sh "docker pull ${env.dockerhubuser}/flaskappproject:latest-dev" // Pull latest-dev image
                    sh "docker tag ${env.dockerhubuser}/flaskappproject:latest-dev ${env.dockerhubuser}/flaskappproject:latest-prod"
                    sh "docker push ${env.dockerhubuser}/flaskappproject:latest-prod" // Push latest-prod image
                }
            }
        }
        stage("Deploy on Server") {
            steps {
                script {
                    if (env.BRANCH_NAME == 'dev') {
                        echo "Deploying Dev Image"
                        sh "docker compose up -d"
                    } else {
                        echo "Deploying Prod Image"
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
