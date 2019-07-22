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
  steps{


  success {



           sshagent(credentials: ["d7:47:30:23:d8:f3:49:37:4a:8d:d3:d8:a0:32:fc:1b"]) {

                                   sh '''git merge master'''
                                   sh '''git push origin master'''
                                   }
    }



  }
}
}
}