variable "name" {
  description = "Nome do cluster AKS"
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

variable "subnet_id" {
  description = "ID da subnet para o AKS"
  type        = string
}

variable "dns_prefix" {
  description = "Prefixo DNS do cluster"
  type        = string
  default     = "agenda"
}

variable "node_count" {
  description = "Número de nodes"
  type        = number
  default     = 1
}

variable "vm_size" {
  description = "Tamanho da VM dos nodes"
  type        = string
  default     = "Standard_D2s_v6"
}

variable "acr_id" {
  description = "ID do ACR para attachment"
  type        = string
  default     = null
}

variable "tags" {
  description = "Tags para o recurso"
  type        = map(string)
  default     = {}
}