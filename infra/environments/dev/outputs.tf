output "resource_group_name" {
  value = module.rg.name
}

output "acr_login_server" {
  value = module.acr.login_server
}

output "aks_name" {
  value = module.aks.name
}

output "postgres_fqdn" {
  value = module.postgres.fqdn
}

output "postgres_database" {
  value = module.postgres.database_name
}

# ✅ Comando para conectar no AKS
output "aks_get_credentials_command" {
  value = "az aks get-credentials --resource-group ${module.rg.name} --name ${module.aks.name}"
}

output "keyvault_name" {
  value = module.keyvault.name
}

output "aks_kubelet_identity_client_id" {
  value     = module.aks.kubelet_identity_client_id
  sensitive = true
}