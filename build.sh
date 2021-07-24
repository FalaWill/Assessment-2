pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                git url: 'https://github.com/FalaWill/Assessment-2.git' 
            }
        }
    }
}
