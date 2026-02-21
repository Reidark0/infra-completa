variable "name" {
  description = "Nome do Key Vault"
  type        = string
}

variable "location" {
  description = "Região Azure"
  type        = string
}

variable "resource_group_name" {
  description = "Nome do Resource Group"
  type        = string
}

variable "postgres_password" {
  description = "Senha do PostgreSQL"
  type        = string
  sensitive   = true
}

variable "postgres_user" {
  description = "Usuário do PostgreSQL"
  type        = string
  default     = "agendaadmin"
}

variable "aks_kubelet_identity_object_id" {
  description = "Object ID do Kubelet Identity do AKS"
  type        = string
}

variable "tags" {
  description = "Tags"
  type        = map(string)
  default     = {}
}