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
                sh "python --version" 
            }
        }
        stage('Deploy') { 
            steps {
                sh "ls -l" 
            }
        }
    }
}
