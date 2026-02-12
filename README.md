# App Web - Calendário
Esta é uma aplicação funcional de calendário com sistema de autenticação, onde o foco principal reside na engenharia de INFRAESTRUTURA de alta disponibilidade. O projeto serve como um laboratório prático para simular ambientes de produção complexos.

## Objetivo
O objetivo deste projeto é implementar uma infraestrutura de nível corporativo em escala reduzida, porém abrangente. O ecossistema integra ferramentas padrão de mercado sob as melhores práticas de Desenvolvimento (Dev), Segurança (Sec) e Operações (Ops).

## Desenvolvimento Auxiliado por IA
Este projeto foi desenvolvido utilizando metodologias de AI-Assisted Engineering. Utilizei inteligência artificial generativa para:
- Revisão de Código e Arquitetura: Validação de padrões de design e estruturas de pacotes Python.
- Pair Programming: Auxílio na escrita de testes unitários e depuração de erros de ambiente.
- Consultoria DevSecOps: Suporte na escolha de ferramentas padrão de mercado e configuração de pipelines de CI/CD.

O uso de IA neste projeto reflete a adoção de ferramentas modernas para acelerar o ciclo de desenvolvimento e garantir a conformidade com as melhores práticas da indústria.


## Stack atual
- Phyton 3.11 (Flask | SQLAlchemy | Pytest)
- Github Actions
- SAST (Semgrep)
- Postgresql 16
- Docker
- Alembic
- Gunicorn


## Status
- Testes unitários
- Esteira Funcional com SAST
- Flask Backend funcional
- PostgreSQL Implementado 
- Docker local


---
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
05/02/2026 - Tudo certo, criando os primeiro os testes para guiar os próximos passos e ter certeza que tudo esta rodando certo.

06/02/2026 - Dia de começar o backend com login e senha. Tantos typos no código que achei que tinha um analfabeto digitando, mas era só eu mesmo

07/02/2026 - Criando os eventos para adicionar no calendario e terminando de arrumar as bagunças de ontem

08/02/2026 - Mermão, quem gosta de programar é maluco, até 4h da manhã e não consegui conectar o backend no banco de dados no Docker

09/02/2026 - mais 3 horas hoje e finalmente descobri o problemam: PostGreSQL rodando localmente há uns 4 anos. Mas depois de resolvido caminhando a passos largos

10/02/2026 - Dia de Dockerizar a aplicação, deu tudo tão certo que acho que tem algum error fazendo tudo dar certo, mas um relogio parado acerta 2x por dia, né?

11/02/2026 - Dia de terminar de resolver problemas na máquina local e adiocionar o Alembic, Gunicorn. ta sendo a parte mais tranquila.

12/02/2026 - 


