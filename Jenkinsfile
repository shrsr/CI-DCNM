pipeline {
agent { docker { image 'gsshreyas/ci:latest' } }

  stages {
    stage('build') {
      steps {
        sh '''python3 -m venv calculator
            . calculator/bin/activate
            pip install -r requirements.txt'''
      }
    }
    stage('test') {
      steps {
        sh '''
            . calculator/bin/activate
            python3 test_dcnmVersion.py
                '''

      }
    }
  }
}
