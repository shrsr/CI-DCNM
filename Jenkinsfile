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




withCredentials([sshUserPrivateKey(credentialsId: 'ssrish', keyFileVariable: 'SSH_KEY')]) {
sh("git init")
sh("git config user.name 'ssrish'")
sh("git config user.email 'ssrish@cisco.com'")
sh("git add .")
sh("git commit -m 'message'")
 sh("git remote remove origin")
  sh("git remote add origin https://github.com/ssrish/Experiment.git")
sh("git checkout -b master")
  sh("git push -u origin master")

}


}
}
}
}