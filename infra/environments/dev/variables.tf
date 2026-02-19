variable "location" {
  description = "Região Azure"
  type        = string
  default     = "Brazil South"
}

variable "postgres_admin_user" {
  description = "Usuário admin do PostgreSQL"
  type        = string
  default     = "agendaadmin"
}

variable "postgres_admin_password" {
  description = "Senha do admin do PostgreSQL"
  type        = string
  sensitive   = true
}