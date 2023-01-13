pipeline {
  agent any

  stages {

    stage("Build") {
      steps {
        sh 'pip install -r requirements.txt' 
        sh 'uvicorn main:app --reload'
      }
    }
    
    stage("Containerize")
    {
        steps {
            sh 'docker --version'
        }
    }
   
    }
}
