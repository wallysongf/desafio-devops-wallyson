Desafio Técnico – DevOps

Repositório com a solução completa para o desafio DevOps. A proposta contempla duas frentes principais:

1. Implementação de uma pipeline de deploy com Jenkins usando estratégia Blue-Green
2. Avaliação e melhoria de uma arquitetura de scraping baseada em AWS Lambda, Docker, Terraform e Selenium

---

Objetivo

Demonstrar capacidade técnica para:

- Arquitetar soluções escaláveis, seguras e performáticas
- Automatizar fluxos de deploy e infraestrutura
- Identificar gargalos e propor melhorias práticas com foco em custo, performance e disponibilidade
- Documentar toda a proposta de forma objetiva, visual e funcional

Parte 1 – Jenkins + Blue-Green Deployment

- Implementação de pipeline CI/CD com Jenkins Pipeline Declarativo
- Deploy em instâncias alternadas (blue/green) com troca controlada via proxy reverso (NGINX)
- Simulação de build/deploy/switch/test com script `deploy.sh`

📄 Documentação detalhada:  
👉 [`README.md`](desafio-1-jenkins/README.md)

📊 Diagrama da arquitetura Jenkins + NGINX:  
👉 [`blue-green-jenkins-nginx.png`](diagramas/blue-green-jenkins-nginx.png)

---

Parte 2 – Scraper AWS com Terraform e Lambda

Arquitetura Atual

- Scraper em Python com Selenium rodando via Docker em AWS Lambda
- Infraestrutura orquestrada com Terraform
- Reação a bloqueios de IP criando novas funções Lambda com novo IP

📄 Análise completa:  
👉 [`README.md`](desafio-2-scraping/README.md)

---

Proposta de Melhoria

- Uso de AWS Lambda via ZIP (sem Docker) para menor cold start
- Orquestração com AWS Step Functions
- Troca de IP dinâmica via NAT Gateway + Elastic IP Pool
- Armazenamento de estado e tentativas via DynamoDB

📄 Documentação da proposta:  
👉 [`README.md`](desafio-2-scraping/README.md)

📊 Diagrama da arquitetura otimizada:  
👉 [`arquitetura-otimizada.png`](diagramas/arquitetura-otimizada.png)

---

Exemplo de Código Python (Lambda)

- Função `scraper.py` detecta IP bloqueado (código HTTP 403) e retorna instruções para retry
- Pode ser usada dentro de Step Functions com retries controlados

📄 [`scraper.py`](desafio-2-scraping/scraper.py)

---

Tecnologias Utilizadas

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

```
./deploy.sh build
./deploy.sh deploy green
./deploy.sh switch green
./deploy.sh test

```

Estimativa Comparativa de Custos

| Item                                   | Arquitetura Atual                             | Arquitetura Otimizada                          |
|----------------------------------------|-----------------------------------------------|------------------------------------------------|
| Execução Lambda (com Docker)       | + Alto cold start<br>+ Tempo limite maior     | - Baixo cold start<br>- Custo por ms menor     |
| Volume de Execuções                | Necessita recriar função Lambda a cada falha  | Reutiliza mesma função com retry controlado     |
| IP Dinâmico (troca de IP)          | Nova função = novo IP (infra duplicada)       | NAT Gateway com IP pool fixo e controlado      |
| Orquestração (Terraform)           | Redeclarações frequentes de recursos          | Step Function coordena com menos criação infra |
| Provisionamento de imagem Docker   | Armazenamento + pull a cada execução          | Nenhum (deploy ZIP leve e rápido)              |

Estimativa geral (AWS)  
Com base em workloads médios (~1000 execuções/dia):

- Arquitetura atual:  
  `US$ 80 a 120/mês` (Lambda com container, recriação, NAT, downloads)

- Arquitetura otimizada:  
  `US$ 25 a 40/mês` (Lambda ZIP, NAT fixo, Step Functions com retry simples)

Redução estimada: ~60–75% no custo total mensal

---

Fontes de referência:

- [AWS Lambda Pricing (oficial)](https://aws.amazon.com/lambda/pricing/)
- [Pricing for Lambda with container images](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-support-for-container-images/)
- [AWS Step Functions Pricing](https://aws.amazon.com/step-functions/pricing/)
- [AWS NAT Gateway Pricing](https://aws.amazon.com/vpc/pricing/)
- [Comparing Lambda ZIP vs. Container Deployments (Medium)](https://medium.com/the-cloud-architect/aws-lambda-deployment-zips-vs-containers-c6b0ee5d4f30)
