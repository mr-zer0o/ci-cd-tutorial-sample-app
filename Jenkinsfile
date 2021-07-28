node{
    stage("SCM Checkout"){
        git credentialsId: 'git-cred', url: 'https://github.com/mr-zer0o/ci-cd-tutorial-sample-app'
    }
    stage("flask build"){
        sh '''

        export WORKSPACE=`pwd`
        virtualenv venv21
        . $WORKSPACE/venv22/bin/activate
        pip install -r requirements.txt
        flask db upgrade

        '''
    }
    stage("Test code"){
        sh '''
            . $WORKSPACE/venv22/bin/activate
            python -m unittest discover
            python seed.py
        '''
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
              docker images -a | grep "zatch/myapp" | awk '{print $3}' | xargs docker rmi -f
            else
              echo "No such container"
            fi

        '''
        def dockerRun = 'docker run -p 8000:8000 -d --name=myapp zatch/myapp:1.0.0'
        sshagent(['dev-server']) {
            sh "ssh -o StrictHostKeyChecking=no ubuntu@3.141.25.1 ${dockerContainerCheck}"
            sh "ssh -o StrictHostKeyChecking=no ubuntu@3.141.25.1 ${dockerRun}"
        }

    }

}