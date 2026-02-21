resource "azurerm_key_vault" "this" {
  name                = var.name
  location            = var.location
  resource_group_name = var.resource_group_name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"
  purge_protection_enabled = false
  enable_rbac_authorization = true

  tags = var.tags
}

data "azurerm_client_config" "current" {}

resource "azurerm_role_assignment" "terraform_kv_admin" {
  scope                = azurerm_key_vault.this.id
  role_definition_name = "Key Vault Secrets Officer"  # Pode criar/ler/deletar secrets
  principal_id         = data.azurerm_client_config.current.object_id
}

resource "azurerm_key_vault_secret" "postgres_password" {
  name         = "postgres-password"
  value        = var.postgres_password
  key_vault_id = azurerm_key_vault.this.id
}

resource "azurerm_key_vault_secret" "postgres_user" {
  name         = "postgres-user"
  value        = var.postgres_user
  key_vault_id = azurerm_key_vault.this.id
}

resource "azurerm_role_assignment" "aks_kv_secrets_user" {
  scope                = azurerm_key_vault.this.id
  role_definition_name = "Key Vault Secrets User"
  principal_id         = var.aks_kubelet_identity_object_id
}