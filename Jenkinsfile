pipeline {
    agent {
        docker {
            image 'ubuntu'
        }
    }
    stages {
        stage('Stage 1') { 
            steps {
                sh "date
            }
        }
        stage('Stage 2') { 
            steps {
//                 sh "python -m unittest -v test"
                sh "who"
            }
        }
        stage('Stage 3') { 
            steps {
                sh "ls -l"
                sh "pwd"
            }
        }
    }
}
