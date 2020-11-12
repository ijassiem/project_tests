pipeline {
    agent any 
    stages {
        stage('clone repo') { 
            steps {
                sh "rm -rf project_tests"
                sh "git clone https://github.com/ijassiem/project_tests.git"
            }
        }
        stage('Test') { 
            steps {
                sh "python -m unittest -v test" 
            }
        }
        stage('Deploy') { 
            steps {
                sh "ls -l"
                sh "pwd"
            }
        }
    }
}
