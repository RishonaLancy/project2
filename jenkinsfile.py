pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Replace with your actual GitHub repository URL
                git branch: 'main', url: 'https://github.com/RishonaLancy/project2.git'
            }
        }
        
        stage('Generate Report') {
            steps {
                // Use 'bat' if running on a Windows agent, or 'sh' if running on Linux/macOS
                bat 'python app.py'
            }
        }
        
        stage('Archive Report') {
            steps {
                // Saves report.txt so it can be downloaded directly from the Jenkins UI
                archiveArtifacts artifacts: 'report.txt', fingerprint: true, onlyIfSuccessful: true
            }
        }
    }
}
