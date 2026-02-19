variable "name" {
  description = "Nome do PostgreSQL server"
  type        = string
}

variable "resource_group_name" {
  description = "Nome do Resource Group"
  type        = string
}

variable "location" {
  description = "Região Azure"
  type        = string
}

variable "admin_user" {
  description = "Usuário admin do PostgreSQL"
  type        = string
}

variable "admin_password" {
  description = "Senha do admin (use Key Vault em prod)"
  type        = string
  sensitive   = true
}

variable "aks_subnet_id" {
  description = "ID da subnet do AKS (para firewall)"
  type        = string
  default     = null
}

variable "tags" {
  description = "Tags para o recurso"
  type        = map(string)
  default     = {}
}