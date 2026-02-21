output "id" {
  value = azurerm_kubernetes_cluster.this.id
}

output "kube_config" {
  value     = azurerm_kubernetes_cluster.this.kube_config_raw
  sensitive = true
}

output "name" {
  value = azurerm_kubernetes_cluster.this.name
}

output "fqdn" {
  value = azurerm_kubernetes_cluster.this.fqdn
}

output "kubelet_identity_object_id" {
  description = "Object ID do Kubelet Identity (para Key Vault)"
  value       = azurerm_kubernetes_cluster.this.kubelet_identity[0].object_id
}

output "kubelet_identity_client_id" {
  description = "Client ID do Kubelet Identity (para CSI Driver)"
  value       = azurerm_kubernetes_cluster.this.kubelet_identity[0].client_id
}