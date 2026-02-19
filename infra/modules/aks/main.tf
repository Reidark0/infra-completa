resource "azurerm_kubernetes_cluster" "this" {
  name                = var.name
  location            = var.location
  resource_group_name = var.resource_group_name
  dns_prefix          = var.dns_prefix

  default_node_pool {
    name           = "default"
    node_count     = var.node_count
    vm_size        = var.vm_size
    vnet_subnet_id = var.subnet_id
  }

  identity {
    type = "SystemAssigned"
  }

  network_profile {
    network_plugin = "azure"
    network_policy = "azure"  
    
    service_cidr       = "10.2.0.0/16"      # Kubernetes Services (interno)
    dns_service_ip     = "10.2.0.10"        # DNS do cluster (dentro do service_cidr)
    # pod_cidr não precisa no Azure CNI
  }

  tags = var.tags
}

resource "azurerm_role_assignment" "aks_to_acr" {
  scope                = var.acr_id
  role_definition_name = "AcrPull"
  principal_id         = azurerm_kubernetes_cluster.this.kubelet_identity[0].object_id

  depends_on = [ azurerm_kubernetes_cluster.this ]
}