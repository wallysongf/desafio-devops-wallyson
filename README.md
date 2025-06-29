Desafio Técnico – DevOps

Repositório com a solução completa para o desafio DevOps. A proposta contempla **duas frentes principais**:

1. Implementação de uma pipeline de deploy com **Jenkins** usando **estratégia Blue-Green**
2. Avaliação e melhoria de uma arquitetura de scraping baseada em **AWS Lambda, Docker, Terraform e Selenium**

---

## 🎯 Objetivo

Demonstrar capacidade técnica para:

- Arquitetar soluções escaláveis, seguras e performáticas
- Automatizar fluxos de deploy e infraestrutura
- Identificar gargalos e propor melhorias práticas com foco em custo, performance e disponibilidade
- Documentar toda a proposta de forma objetiva, visual e funcional

---

Estrutura do Repositório

├── jenkins-deploy/ # Parte 1 – Jenkins + Blue-Green
│ ├── Jenkinsfile
│ ├── deploy.sh
│ ├── README.md
│ └── diagramas/
│ └── blue-green-jenkins-nginx.png
│
├── scraper-otimizado/ # Parte 2 – Scraping AWS Lambda
│ ├── scraper.py
│ ├── infra-original.md
│ ├── infra-melhorada.md
│ └── diagramas/
│ ├── arquitetura-atual.png
│ └── arquitetura-otimizada.png

---

## 🧩 Parte 1 – Jenkins + Blue-Green Deployment

- Implementação de pipeline CI/CD com Jenkins Pipeline Declarativo
- Deploy em instâncias alternadas (blue/green) com troca controlada via proxy reverso (NGINX)
- Simulação de build/deploy/switch/test com script `deploy.sh`

📄 Documentação detalhada:  
👉 [`jenkins-deploy/README.md`](jenkins-deploy/README.md)

📊 Diagrama da arquitetura Jenkins + NGINX:  
👉 [`blue-green-jenkins-nginx.png`](jenkins-deploy/diagramas/blue-green-jenkins-nginx.png)

---

## 🔎 Parte 2 – Scraper AWS com Terraform e Lambda

### 🔹 Arquitetura Atual

- Scraper em Python com Selenium rodando via Docker em AWS Lambda
- Infraestrutura orquestrada com Terraform
- Reação a bloqueios de IP criando novas funções Lambda com novo IP

📄 Análise completa:  
👉 [`scraper-otimizado/infra-original.md`](scraper-otimizado/infra-original.md)

📊 Diagrama da arquitetura atual:  
👉 [`arquitetura-atual.png`](scraper-otimizado/diagramas/arquitetura-atual.png)

---

### 🛠️ Proposta de Melhoria

- Uso de AWS Lambda via ZIP (sem Docker) para menor cold start
- Orquestração com AWS Step Functions
- Troca de IP dinâmica via NAT Gateway + Elastic IP Pool
- Armazenamento de estado e tentativas via DynamoDB

📄 Documentação da proposta:  
👉 [`scraper-otimizado/infra-melhorada.md`](scraper-otimizado/infra-melhorada.md)

📊 Diagrama da arquitetura otimizada:  
👉 [`arquitetura-otimizada.png`](scraper-otimizado/diagramas/arquitetura-otimizada.png)

---

## 🧪 Exemplo de Código Python (Lambda)

- Função `scraper.py` detecta IP bloqueado (código HTTP 403) e retorna instruções para retry
- Pode ser usada dentro de Step Functions com retries controlados

📄 [`scraper-otimizado/scraper.py`](scraper-otimizado/scraper.py)

---

## 🛠️ Tecnologias Utilizadas

- Jenkins
- Shell Script
- AWS Lambda (com e sem Docker)
- Terraform
- AWS Step Functions
- VPC + NAT Gateway + Elastic IP
- Python (Requests/Selenium)
- DynamoDB (para estado)
- Draw.io e DALL·E para os diagramas

---

Jenkins

```bash
# Executar local com simulação
./deploy.sh build
./deploy.sh deploy green
./deploy.sh switch green
./deploy.sh test
