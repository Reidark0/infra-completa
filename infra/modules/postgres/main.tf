resource "azurerm_postgresql_flexible_server" "this" {
  name                   = var.name
  resource_group_name    = var.resource_group_name
  location               = var.location
  version                = "16"
  administrator_login    = var.admin_user
  administrator_password = var.admin_password
  storage_mb             = 32768
  sku_name               = "B_Standard_B1ms"
  zone                   = "3"

  tags = var.tags
}

resource "azurerm_postgresql_flexible_server_firewall_rule" "allow_all" {
  name             = "allow-all-dev"
  server_id        = azurerm_postgresql_flexible_server.this.id
  start_ip_address = "0.0.0.0" 
  end_ip_address   = "255.255.255.255"
}

resource "azurerm_postgresql_flexible_server_database" "agenda" {
  name      = "agenda"
  server_id = azurerm_postgresql_flexible_server.this.id
  charset   = "UTF8"
  collation = "en_US.utf8"
}