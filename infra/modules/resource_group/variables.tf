variable "name" {
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