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
                    image 'node:16-buster'
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
                            docker-compose -f docker-compose-cicd.yml --project-name "$JOB_NAME/$BUILD_NUMBER" up --build --abort-on-container-exit --exit-code-from selenium-python-tests
                            rm requirements*.txt
                            cd tests/selenium_tests
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
                      docker-compose -f docker-compose-cicd.yml --project-name "$JOB_NAME/$BUILD_NUMBER" down
                    '''

                    junit '**/junit.xml'

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
