pipeline {
  agent { docker { image 'gsshreyas/ci:latest' } }
  stages {

  stage('Input') {
    steps {
      script {
                   env.RELEASE_SCOPE = input message: 'Enter Fabric', ok: 'Release!',


                echo "${env.RELEASE_SCOPE}"
            }
    }
}


    stage('build') {
      steps {
        sh '''python3 -m venv virtual
            . virtual/bin/activate
            pip install -r requirements.txt'''

      }
    }
    stage('test') {
      steps {
        sh '''
            . virtual/bin/activate
            python3 testNetwork.py
                '''

      }
    }
  }
}