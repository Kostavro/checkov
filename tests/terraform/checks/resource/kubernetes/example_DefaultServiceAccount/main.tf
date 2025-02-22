resource "kubernetes_service_account" "fail" {
  metadata {
    name = "default"
  }
}

resource "kubernetes_service_account" "fail2" {
  metadata {
    name = "default"
  }
  automount_service_account_token=true
}

resource "kubernetes_service_account" "pass" {
  metadata {
    name = "default"
  }
  automount_service_account_token=false
}

resource "kubernetes_service_account" "pass2" {
  metadata {
    name = "terraform-example"
  }
}
