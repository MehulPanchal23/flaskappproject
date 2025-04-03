pipeline {
    agent { 
        label (env.JOB_NAME.contains('dev') ? 'Dev' : 'Prod')
    }
    environment {
        // Temporary static placeholders; real values will be set in script block
        BRANCH_NAME = ''
        IMAGE_TAG = ''
    }
    stages {
        stage("Set Environment Variables"){
            steps {
                script {
                    env.BRANCH_NAME = env.JOB_NAME.contains('dev') ? 'dev' : 'master'
                    env.IMAGE_TAG = env.JOB_NAME.contains('dev') ? 'latest-dev' : 'latest-prod'
                }
            }
        }
        stage("Code Clone from GitHub") {
            steps {
                script {
                    echo "Cloning branch: ${BRANCH_NAME}"
                    git url: "https://github.com/MehulPanchal23/flaskappproject.git", branch: BRANCH_NAME
                }
            }
        }
        stage("Build Docker Image") {
            steps {
                sh "docker build -t flaskappproject:${IMAGE_TAG} ."
            }
        }
        stage("Push Image to Docker HUB") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: "dockerhubcred",
                    passwordVariable: "dockerhubpass",
                    usernameVariable: "dockerhubuser"
                )]) {
                    sh "docker login -u ${env.dockerhubuser} -p ${env.dockerhubpass}"
                    sh "docker tag flaskappproject:${IMAGE_TAG} ${env.dockerhubuser}/flaskappproject:${IMAGE_TAG}"
                    sh "docker push ${env.dockerhubuser}/flaskappproject:${IMAGE_TAG}"
                }
            }
        }
        stage("Deploy on Server") {
            steps {
                script {
                    if (BRANCH_NAME == 'master') {
                        echo "Deploying Production Image"
                        sh "docker pull ${env.dockerhubuser}/flaskappproject:latest-dev" // Pull dev image in prod
                        sh "docker tag ${env.dockerhubuser}/flaskappproject:latest-dev flaskappproject:prod"
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
                     subject: "Build Successful: ${BRANCH_NAME}",
                     body: "Build and Deployment Successful for ${BRANCH_NAME}",
                     to: "panchalmehul195@gmail.com"
        }
        failure {
            emailext from: "panchalmehul191@gmail.com",
                     subject: "Build Failed: ${BRANCH_NAME}",
                     body: "Check Logs for Errors in ${BRANCH_NAME}",
                     to: "panchalmehul195@gmail.com"
        }
    }
}
