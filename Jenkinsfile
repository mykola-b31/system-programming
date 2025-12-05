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
						dpkg -i ../count-files_*.deb
						
						echo "Executing script from package"
						count_files
						
						echo "Uninstalling DEB package"
						dpkg -r count-files
					'''
                }
            }
        }

        stage('Build & Test RPM') {
            steps {
                script {
					sh '''
						echo "Building RPM package"
                    
                        mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
                        cp count_files.sh ~/rpmbuild/SOURCES/
                        cp rpm/count_files.spec ~/rpmbuild/SPECS/
						
						rpmbuild -bb ~/rpmbuild/SPECS/count_files.spec
						
						echo "Installing RPM package"
						rpm -ivh --force ~/rpmbuild/RPMS/noarch/count_files-*.rpm
						
						echo "Executing script from package"
						count_files
						
						echo "Uninstalling RPM package"
						rpm -e count_files
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
