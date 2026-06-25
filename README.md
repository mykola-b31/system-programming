# System Programming: CI/CD & Linux Packaging

![Build Status](https://github.com/mykola-b31/system-programming/actions/workflows/build.yml/badge.svg)

This repository demonstrates a complete CI/CD workflow for automating the build, testing, and packaging of a Linux utility. It transforms a simple Bash script into native installer packages for both Debian-based and RedHat-based distributions.

## Tech Stack

![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Debian](https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

## Key Features

* **Automated Packaging:** Includes fully configured specification and control files to build `.deb` and `.rpm` packages.
* **Jenkins Pipeline:** A declarative `Jenkinsfile` that automates the building of both DEB and RPM packages. The pipeline also tests the packages by installing them, executing the script, and uninstalling them to ensure end-to-end reliability.
* **GitHub Actions:** CI workflow configured to automatically build and upload DEB and RPM packages as workflow artifacts on pushes and pull requests to the `main` branch.
* **Dockerized Infrastructure:** Contains a `docker-compose.yml` and a custom Dockerfile to spin up a Jenkins Master and a dedicated Jenkins SSH agent pre-installed with all necessary build tools (`dpkg-buildpackage`, `rpmbuild`, etc.).

## Project Structure

* `.github/workflows/` - GitHub Actions configuration for automated builds.
* `debian/` - Configuration files (control, rules, changelog, etc.) for building the DEB package.
* `rpm/` - Spec file for building the RPM package.
* `docker/` - Docker Compose and Dockerfile for deploying the Jenkins CI/CD environment locally.
* `Jenkinsfile` - The pipeline definition for Jenkins CI.
* `count_files.sh` - The core application script.

## Infrastructure Setup (Local CI/CD)

To run the Jenkins pipeline locally, you can spin up the provided Docker environment:

1. Navigate to the `docker` directory.
2. Export your Jenkins agent's public SSH key as an environment variable: `export JENKINS_AGENT_SSH_PUBKEY="ssh-rsa AAAA..."`.
3. Run `docker-compose up -d` to start the Jenkins Master and Agent nodes.
4. Configure the pipeline in Jenkins pointing to this repository.

### Tested On

* Ubuntu 22.04 (GitHub Actions runner and Jenkins agent base)
* Docker Compose file format 3.8
* `jenkins/jenkins:lts` and `jenkins/ssh-agent:latest-jdk17` images

## About the Core Script

The utility being packaged is a Bash script designed to count files within the `/etc` directory and its subdirectories. 

### Manual Script Usage

If you want to run the script directly without installing the packages:

```bash
chmod +x count_files.sh
sudo ./count_files.sh
```

Example output:

```
Number of files in /etc: 102
Number of files in subdirs: 1777
Total files in /etc: 1879
```

> ⚠️ Important: Run the script with sudo to ensure access to all directories inside /etc. Without sudo, the script may show fewer files due to restricted access permissions.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
