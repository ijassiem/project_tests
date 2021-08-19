pipeline {
    agent {
        docker { image 'ubuntu'}
    }
    stages {
        stage('Stage 1') { 
            steps {
                sh "date"
            }
        }
        stage('Stage 2') { 
            steps {
                sh "lsb_release -a"
                sh "python --version"
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
