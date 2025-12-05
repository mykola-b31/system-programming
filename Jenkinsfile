pipeline {
    agent { 
        label 'builder' 
    }

    options {
        timeout(time: 5, unit: 'MINUTES')
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }

        stage('Build & Test DEB') {
            steps {
                script {
                    sh '''
                        echo "Building DEB package"
                        dpkg-buildpackage -us -uc -b

                        echo "Installing DEB package"
                        sudo dpkg -i ../count-files_*.deb

                        echo "Executing script from package"
                        sudo count_files.sh

                        echo "Uninstalling DEB package"
                        sudo dpkg -r count-files
                    '''
                }
            }
        }

        stage('Build & Test RPM') {
            steps {
                script {
                    sh '''
                        echo "Building RPM package"

                        mkdir -p \
                            ~/rpmbuild/BUILD \
                            ~/rpmbuild/RPMS \
                            ~/rpmbuild/SOURCES \
                            ~/rpmbuild/SPECS \
                            ~/rpmbuild/SRPMS
                            
                        cp count_files.sh ~/rpmbuild/SOURCES/
                        cp rpm/count_files.spec ~/rpmbuild/SPECS/

                        rpmbuild -bb ~/rpmbuild/SPECS/count_files.spec

                        echo "Installing RPM package"
                        sudo rpm -ivh --force --nodeps ~/rpmbuild/RPMS/noarch/count_files-*.rpm

                        echo "Executing script from package"
                        sudo count_files

                        echo "Uninstalling RPM package"
                        sudo rpm -e count_files
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Both DEB and RPM packages were built and tested successfully.'
        }
        failure {
            echo 'Something went wrong.'
        }
        always {
            cleanWs()
            sh 'rm -f ../count-files_*'
        }
    }
}
