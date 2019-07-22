pipeline {
  agent { docker { image 'gsshreyas/ci:latest' } }
  stages {



    stage('build') {
      steps {
        sh '''python3 -m venv virtual
            . virtual/bin/activate
            pip install -r requirements.txt'''

      }
    }

  stage('Validate Latest Version Of DCNM') {

  steps {
  sh '''
    . virtual/bin/activate
    python3 test_dcnmVersion.py
      '''

  }
}

    stage('Test Network Deplyement Status') {

      steps {
        sh '''
            . virtual/bin/activate
            python3 testNetwork.py
                '''

      }
    }
  stage('Develop'){
  post {
  steps{
  success {
          git url: "https://wwwin-github.cisco.com/ssrish/CI.git",
           credentialsId: 'jenkins_ssh_key',
           branch: develop
           sh 'git tag -a tagName -m "Your tag comment"'
           sh 'git merge develop'
           sh 'git commit -am "Merged develop branch to master'
           sh "git push origin master"
    }
  failure {
      mail to: 'ssrish@cisco.com', subject: 'The Pipeline failed :('
    }

    }
  }
}
