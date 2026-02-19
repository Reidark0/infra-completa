variable "name" {
  description = "Nome do ACR"
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

variable "tags" {
  description = "Tags para o recurso"
  type        = map(string)
  default     = {}
}