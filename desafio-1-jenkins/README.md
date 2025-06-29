# Jenkins + Blue-Green Deployment

Este módulo simula uma pipeline de deploy com Jenkins utilizando a estratégia Blue-Green.

Pipeline

1. Build da aplicação
2. Deploy na instância inativa (blue ou green)
3. Switch do proxy reverso para a instância nova
4. Testes pós-deploy

Script

O script deploy.sh simula os passos do pipeline. Na prática, ele seria responsável por:

- Fazer build com Docker
- Realizar o deploy em instâncias blue/green
- Atualizar o proxy reverso (NGINX)
- Executar testes básicos

Jenkinsfile

A pipeline está escrita em formato Declarativo e pode ser executada em um agente Jenkins simples.

Diagrama da Arquitetura

![Diagrama Jenkins Blue-Green](diagramas/blue-green-jenkins-nginx.png)

