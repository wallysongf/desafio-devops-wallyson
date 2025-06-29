Arquitetura Atual – Sistema de Scraping com AWS, Docker e Terraform

Este documento descreve a arquitetura original proposta no desafio, utilizada para executar um scraper em ambiente cloud usando AWS.

---

Componentes Atuais

- Python com Selenium: linguagem e biblioteca de scraping
- Docker: empacotamento da aplicação + dependências
- AWS Lambda: função executada via imagem Docker
- Terraform: infraestrutura como código para criação de recursos e orquestração

---

Lógica de Execução

1. Um scraper em Python (usando Selenium) é empacotado como uma imagem Docker.
2. Essa imagem é executada dentro de uma função Lambda.
3. Durante o scraping, se ocorrer um bloqueio de IP, o código detecta a falha (ex: erro 403).
4. Nesse caso, o Terraform é acionado para provisionar:
   - Uma nova Lambda
   - Um novo IP associado à VPC
5. O código recomeça a raspagem na nova função.

---

Pontos Críticos

| Limitação      | Descrição                                                           |
|----------------|---------------------------------------------------------------------|
| Custo          | Docker + Lambda = cold start elevado + recursos caros               |
| Performance    | Toda mudança de IP exige nova Lambda                                |
| Escalabilidade | Arquitetura é sequencial, pouco paralelizável                       |
| Manutenção     | Terraform em execução contínua não é o ideal para fluxo de controle |
 