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

           git url: "https://wwwin-github.cisco.com/ssrish/Experiment.git",
           credentialsId: 'Jenkins',
           branch: master
           sh '''git merge master'''
           sh '''git commit -m "TEST"'''
           sh '''git push origin master'''
    }



  }
}
}
}