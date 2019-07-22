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

    stage('Test Network's Deplyement Status') {

      steps {
        sh '''
            . virtual/bin/activate
            python3 testNetwork.py
                '''

      }
    }
  }
}