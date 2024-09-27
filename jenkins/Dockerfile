FROM jenkins/jenkins:lts

USER root

# Atualiza os pacotes e instala o Docker
RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get clean

# Adiciona o usuário Jenkins ao grupo Docker
RUN usermod -aG docker jenkins

# Retorna ao usuário padrão do Jenkins
USER jenkins