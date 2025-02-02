terraform {
    required_providers {
        azurerm = {
            source = "hashicorp/azurerm"
            version = "=4.17.0"
        }
    }
}

provider "azurerm" {
    subscription_id = var.subscription_id
    features {}
}

# Create a resource group
resource "azurerm_resource_group" "rg_sudoku" {
  name     = "rg-sudoku"
  location = "West Europe"
}
