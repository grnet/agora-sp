pipeline {
    agent any
    options {
        checkoutToSubdirectory('agora-sp')
    }
    environment {
        PROJECT_DIR = 'agora-sp'
        GH_USER = 'newgrnetci'
        GH_EMAIL = '<argo@grnet.gr>'
    }
    stages {
        stage ('Deploy Docs') {
            when {
                anyOf {
                    changeset 'docs/**'
                    changeset 'website/**'
                }
            }
            agent {
                docker {
                    image 'node:buster'
                }
            }
            steps {
                echo 'Publish agora docs...'
                sh '''
                    cd $WORKSPACE/$PROJECT_DIR
                    cd website
                    npm install
                '''
                sshagent (credentials: ['jenkins-master']) {
                    sh '''
                        cd $WORKSPACE/$PROJECT_DIR/website
                        mkdir ~/.ssh && ssh-keyscan -H github.com > ~/.ssh/known_hosts
                        git config --global user.email ${GH_EMAIL}
                        git config --global user.name ${GH_USER}
                        GIT_USER=${GH_USER} USE_SSH=true npm run deploy
                    '''
                }
            }
        }
        stage ('Run Tests') {
            steps {
                withCredentials(bindings: [string(credentialsId: 'tinyMCE_key', variable: 'TINYMCEKEY')]) {
                    sh 'sed -i "s/my-api-key/${TINYMCEKEY}/g" $WORKSPACE/$PROJECT_DIR/ui/config/environment.js'
                }
                echo 'Create docker containers...'
                sh '''
                    cd $WORKSPACE/$PROJECT_DIR
                    docker-compose up -d --build
                    rm requirements*.txt
                    cd tests/selenium_tests
                    pipenv install -r requirements.txt
                    echo "Wait for argo container to initialize"
                    while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:8000/ui/auth/login)" != "200" ]]; do if [[ "$(docker ps | grep agora | wc -l)" != "2" ]]; then exit 1; fi; sleep 5; done
                    pipenv run python agora_ui_tests.py --url http://localhost:8000/
                '''
            }
            post {
                always {
                    sh '''
                      cd $WORKSPACE/$PROJECT_DIR
                      docker-compose -f docker-compose-selenium-test.yml down
                      cd tests/selenium_tests
                      pipenv --rm
                    '''
                    cleanWs()
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        success {
            script {
                if ( env.BRANCH_NAME == 'master' || env.BRANCH_NAME == 'devel' ) {
                    slackSend( message: ":rocket: New version for <$BUILD_URL|$PROJECT_DIR>:$BRANCH_NAME Job: $JOB_NAME !")
                }
            }
        }
        failure {
            script {
                if ( env.BRANCH_NAME == 'master' || env.BRANCH_NAME == 'devel' ) {
                    slackSend( message: ":rain_cloud: Build Failed for <$BUILD_URL|$PROJECT_DIR>:$BRANCH_NAME Job: $JOB_NAME")
                }
            }
        }
    }
}
