node{
    stage("SCM Checkout"){
        git credentialsId: 'git-cred', url: 'https://github.com/mr-zer0o/ci-cd-tutorial-sample-app'
    }
    stage("flask build"){
        sh '''


        export WORKSPACE=`pwd`
        virtualenv venv1
        . $WORKSPACE/venv1/bin/activate
        pip install -r requirements.txt
        flask db upgrade
        python seed.py

        '''
    }
    stage("Test code"){
        sh '''
            . $WORKSPACE/venv1/bin/activate
            python -m unittest discover
        '''
    }
    stage("SonarQube Analysis"){
        sh 'echo N/A'
    }

    stage("Build docker Image"){
        sh 'docker build -t zatch/myapp:1.0.0 $WORKSPACE'
    }
    stage("Push Docker Image"){
        withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerHubPwd')]) {
            sh "docker login -u zatch -p ${dockerHubPwd}"
        }
        sh 'docker push zatch/myapp:1.0.0'
    }
    stage("Run container on dev server"){
        def dockerContainerCheck = '''
            result=$(docker ps -f name=myapp -q -a)
            if [[ -n "$result" ]]; then
              docker ps -f name=myapp -q -a | xargs --no-run-if-empty docker container stop | xargs docker container rm
            else
              echo "No such container"
            fi
        '''
        def dockerRun = 'docker run -p 8000:8000 -d --name=myapp zatch/myapp:1.0.0'
        sshagent(['dev-server']) {
            sh "ssh -o StrictHostKeyChecking=no ubuntu@3.133.133.82 ${dockerContainerCheck}"
            sh "ssh -o StrictHostKeyChecking=no ubuntu@3.133.133.82 ${dockerRun}"
        }

    }

}