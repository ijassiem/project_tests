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
                sh "ps"
//                 sh "docker image ls"
//                 sh "docker ps"
                script {
                    branch = env.BRANCH_NAME
                    //tag = (branch == "main") ? "latest" : branch
                    echo "The branch is ${branch}"
                    echo "The commit is ${GIT_COMMIT}"
                }
            }
        }
    }
}
