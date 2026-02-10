# App Web - Calendário
A aplicação é simples, apenas um cadastro com login e senha para um calendário 
a MAGIA vai acontecer por baixo dos panos, na **INFRAESTRUTURA**. O plano é ela ser de nível corporativo.
No final esse projeto vai contar boas práticas de desenvolvimento, segurança e operação.

## Objetivo
Foco no processo, a complexidade vai ser na infra, não na aplicação


## Stack atual
- Phyton 3.11
- Flask
- Pytest
- Github Actions
- SAST (Semgrep)


## Status
- Esteira Básica
- Flask Backend funcional
- Testes unitários
- PostgreSQL inicial
- Dockerlocal


# Previsão das ferramentas que vão ser usadas 
### Cloud Azure 
- Azure Subscription
- Resource Groups
- Azure Virtual Network (VNet)
- Subnets
- Network Security Group (NSG)
- Azure Standard Load Balancer
- Azure PostgreSQL Flexible Server
- Azure Key Vault
- Azure DNS
- Azure Private Endpoint
- Azure Private DNS Zone
- Private DNS VNet Link
- Azure Blob Storage


### Kubernetes (Cluster & Ingress)
- Azure Kubernetes Service (AKS)
- NGINX Ingress Controller
- cert-manager
- Metrics Server
- Kustomize


### Observabilidade
- Prometheus
- Grafana
- Log Analytics Workspace
- Container Insights
- Azure Monitor


### GitOps / CI/CD / Segurança
- Git (SCM)
- GitHub
- GitHub Actions
- Argo CD
- Semgrep
- OWASP ZAP
- Azure Policy
- Azure RBAC
- Key Vault RBAC
- Azure Tags & Naming Standards


### TLS / ACME / Certificados
- Let’s Encrypt
- acme.sh
- PFX (Key Vault Certificates)


### Infra como Código / Automação
- OpenTofu
- Terraform Language (.tf)
- Ansible


### Bastion / Operação
- Bastion
- kubectl
- helm
- psql
- dig
- nslookup
- SSH


### Aplicação / Desenvolvimento
- Python
- Flask
- Docker
- pytest


## Conhecimentos técnicos usados
- Redes Azure (VNet/Private Link/DNS privado)
- AKS avançado (Spot nodes, autoscaler, Ingress, TLS)
- GitOps (Argo CD)
- CI/CD com GitHub Actions
- SAST/DAST
- Automação com Ansible
- TLS/Certificados/ACME
- Key Vault
- Infra como Código
- Monitoramento e debugging básico (nginx logs, kubectl)
- Repositórios
- RBAC

05/02/2026 - Tudo certo, criando os primeiros passos do Flask
06/02/2026 - Dia de começar o backend com login e senha. Tantos typos no código que achei que tinha um analfabeto digitando, mas era só eu mesmo
07/02/2026 - Criando os eventos para adicionar no calendario e terminando de arrumar as bagunças de ontem
08/02/2026 - Mermão, quem gosta de programar é maluco, até 4h da manhã e não consegui conectar o backend no banco de dados
09/02/2026 - 1h da manhã descobri o problema de ontem: PostGreSQL rodando localmente há uns 4 anos. Mas depois de resolvido caminhando a passos largos
10/02/2026 - 
