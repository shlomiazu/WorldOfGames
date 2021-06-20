pipeline {
    agent any
    stages {
        stage('connect to git') {
            steps {
                git 'https://github.com/shlomiazu/MySoftware.git'
            }
        }
        stage('Get DockerFile to Build img') {
            steps {
                bat 'docker build -t wog-score-img .'
            }
        }
        stage('run Docker from img ') {
            steps {
                bat 'docker run -d -p 8777:8777 --name wog-container wog-score-img:latest'
            }
        }
        stage('run e2e for selenium  ') {
            steps {
                 bat 'python e2e.py'
            }
        }
        stage('push to DockerHub') {
            steps {
                 bat 'docker tag games shminaz/scores_of_wog'
                 bat 'docker push shlomiaz/wog_rep'
            }
        }
        stage('rm to container & img') {
            steps {
                 bat 'docker rm -vf wog-container'
                 bat 'docker image rm -f wog-score-img'
            }
        }
   
    }
}
