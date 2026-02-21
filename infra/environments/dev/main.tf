terraform {
  required_version = ">= 1.5"
  
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# ✅ Locals para nomes consistentes
locals {
  env    = "dev"
  prefix = "agenda-${local.env}"
  
  common_tags = {
    Environment = local.env
    Project     = "Agenda"
    ManagedBy   = "Terraform"
  }
}

# Resource Group
module "rg" {
  source   = "../../modules/resource_group"
  name     = "${local.prefix}-rg"
  location = var.location
  tags     = local.common_tags
}

# Network
module "network" {
  source              = "../../modules/network"
  vnet_name           = "${local.prefix}-vnet"
  location            = module.rg.location
  resource_group_name = module.rg.name
}

# ACR
module "acr" {
  source              = "../../modules/acr"
  name                = replace("${local.prefix}acr", "-", "")  # ACR não aceita hífen
  resource_group_name = module.rg.name
  location            = module.rg.location
  tags                = local.common_tags
}

# AKS
module "aks" {
  source              = "../../modules/aks"
  name                = "${local.prefix}-aks"
  location            = module.rg.location
  resource_group_name = module.rg.name
  subnet_id           = module.network.subnet_id
  acr_id              = module.acr.id  # ✅ Attachment
  tags                = local.common_tags

  depends_on = [ module.acr ]
}

# PostgreSQL
module "postgres" {
  source              = "../../modules/postgres"
  name                = "${local.prefix}-postgres"
  resource_group_name = module.rg.name
  location            = module.rg.location
  admin_user          = var.postgres_admin_user
  admin_password      = var.postgres_admin_password
  tags                = local.common_tags
}

module "keyvault" {
  source = "../../modules/keyvault"
  
  name                = "${local.prefix}-kv"
  location            = module.rg.location
  resource_group_name = module.rg.name
  
  postgres_password = var.postgres_admin_password
  postgres_user     = var.postgres_admin_user
  
  aks_kubelet_identity_object_id = module.aks.kubelet_identity_object_id
  
  tags = local.common_tags
  
  depends_on = [module.aks]
}
