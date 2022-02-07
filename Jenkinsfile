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
                sh "cat /etc/*release"
            }
        }
        stage('Stage 3') { 
            steps {
                sh "ls -l"
                sh "pwd"
                sh "whoami"
                sh "hostname"
//                 sh "docker image ls"
//                 sh "docker ps"
            }
        }
    }
}
