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
- Esteira Funcional com SAST
- Flask Backend funcional
- Testes unitários
- PostgreSQL Implementado 
- Docker local



# Previsão das ferramentas que vão ser usadas 
| Cloud Azure | Kubernetes (Cluster & Ingress) | Observabilidade | GitOps / CI/CD / Segurança | TLS / ACME / Certificados | Infra como Código / Automação | Bastion / Operação | Aplicação / Desenvolvimento |
|---|---|---|---|---|---|---|---|
| Azure Subscription | Azure Kubernetes Service (AKS) | Prometheus | Git (SCM) | Let’s Encrypt | OpenTofu | Bastion | Python |
| Resource Groups | NGINX Ingress Controller | Grafana | GitHub | acme.sh | Terraform Language (.tf) | kubectl | Flask |
| Azure Virtual Network (VNet) | cert-manager | Log Analytics Workspace | GitHub Actions | PFX (Key Vault Certificates) | Ansible | helm | Docker |
| Subnets | Metrics Server | Container Insights | Argo CD |  |  | psql | pytest |
| Network Security Group (NSG) | Kustomize | Azure Monitor | Semgrep |  |  | dig |  |
| Azure Standard Load Balancer |  |  | OWASP ZAP |  |  | nslookup |  |
| Azure PostgreSQL Flexible Server |  |  | Azure Policy |  |  | SSH |  |
| Azure Key Vault |  |  | Azure RBAC |  |  |  |  |
| Azure DNS |  |  | Key Vault RBAC |  |  |  |  |
| Azure Private Endpoint |  |  | Azure Tags & Naming Standards |  |  |  |  |
| Azure Private DNS Zone |  |  |  |  |  |  |  |
| Private DNS VNet Link |  |  |  |  |  |  |  |
| Azure Blob Storage |  |  |  |  |  |  |  |


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
----
# Diário 
05/02/2026 - Tudo certo, criando os primeiros passos do Flask

06/02/2026 - Dia de começar o backend com login e senha. Tantos typos no código que achei que tinha um analfabeto digitando, mas era só eu mesmo

07/02/2026 - Criando os eventos para adicionar no calendario e terminando de arrumar as bagunças de ontem

08/02/2026 - Mermão, quem gosta de programar é maluco, até 4h da manhã e não consegui conectar o backend no banco de dados no Docker

09/02/2026 - mais 3 horas hoje e finalmente descobri o problemam: PostGreSQL rodando localmente há uns 4 anos. Mas depois de resolvido caminhando a passos largos

10/02/2026 - Dia de Dockerizar a aplicação




