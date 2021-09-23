def testBuildBadge = addEmbeddableBadgeConfiguration(id: "teststatus", subject: "Selenium Tests")

pipeline {
    agent any
    options {
        checkoutToSubdirectory('agora-sp')
    }
    environment {
        PROJECT_DIR = 'agora-sp'
        GH_USER = 'newgrnetci'
        GH_EMAIL = '<argo@grnet.gr>'
        RAND_PORT = sh(script: "echo 3333",returnStdout: true).trim()
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
                script
                {
                    testBuildBadge.setStatus('running')
                    testBuildBadge.setColor('blue')

                    try
                    {
                        withCredentials(bindings: [string(credentialsId: 'tinyMCE_key', variable: 'TINYMCEKEY')])
                        { sh 'sed -i "s/my-api-key/${TINYMCEKEY}/g" $WORKSPACE/$PROJECT_DIR/ui/config/environment.js' }

                        echo 'Create docker containers...'
                        sh '''
                            cd $WORKSPACE/$PROJECT_DIR
                            sed  "s/8000/${RAND_PORT}/g" agora/docker/deployment.conf
                            echo "RAND_PORT=$RAND_PORT" > .env
                            docker-compose -p $JOB_NAME -f docker-compose-cicd.yml up -d --build
                            rm requirements*.txt
                            cd tests/selenium_tests
                            pipenv install -r requirements.txt
                            echo "Wait for argo container to initialize"
                            while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:${RAND_PORT}/ui/auth/login)" != "200" ]]; do if [[ "$(docker ps | grep agora | wc -l)" != "2" ]]; then exit 1; fi; sleep 5; done
                            pipenv run pytest agora_unit_tests.py --port ${RAND_PORT} -o junit_family=xunit2 --junitxml=reports/junit.xml
                        '''

                        testBuildBadge.setStatus('passing')
                        testBuildBadge.setColor('brightgreen')
                    }
                    catch (Exception err)
                    {
                        testBuildBadge.setStatus('failing')
                        testBuildBadge.setColor('red')
                    }
                }
            }
            post {
                always {
                    sh '''
                      cd $WORKSPACE/$PROJECT_DIR
                      docker-compose -p $JOB_NAME -f docker-compose-cicd.yml down
                    '''

                    junit '**/junit.xml'

                    sh '''
                      cd $WORKSPACE/$PROJECT_DIR
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
