//
////We will create a Pipeline
//pipeline{
//    agent any //we specify the the agent(current Jenkins server)
//
//    stages { //dev, uat etc
//        stage ('Dev'){
//            steps {
//                echo 'Hello World'
//                echo 'Hello World again'
//            }
//        }
//    }
//}

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/robertcrozierw-spec/InvadePythonGitHub.git'
                
            }
        }
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build("bobcorp/invadepython:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'git') {            
                    dockerImage.push("${env.BUILD_NUMBER}")            
                    dockerImage.push("latest")    
                    }
                }
            }
        }
    }
}