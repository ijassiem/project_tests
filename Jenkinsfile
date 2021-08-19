pipeline {
    agent {
        docker { image 'ubuntu' args '-u=root'}
    }
    stages {
        stage('Stage 1') { 
            steps {
                sh "date"
            }
        }
        stage('Stage 2') { 
            steps {
                sh "cat /etc/*release"
            }
        }
        stage('Stage 3') { 
            steps {
                sh "ls -l"
                sh "pwd"
                sh "docker image ls"
                sh "docker ps"
            }
        }
    }
}
