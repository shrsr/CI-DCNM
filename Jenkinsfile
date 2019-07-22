pipeline {
  agent { docker { image 'gsshreyas/ci:latest' } }
  stages {

  stage('Input') {
  input{
  message "Press Ok to continue"
  submitter "user1,user2"
  parameters {
    string(name:'username', defaultValue: 'user', description: 'Username of the user pressing Ok')
  }
  }
  steps {
    echo "User: ${username} said Ok."
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