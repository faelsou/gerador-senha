FROM jenkins/jenkins:lts

USER root

# Instala o Docker
RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get clean

# Retorna ao usuário padrão do Jenkins
USER jenkinsFROM jenkins/jenkins:lts
USER root
RUN mkdir -p /var/lib/apt/lists/partial
RUN apt update
USER jenkins