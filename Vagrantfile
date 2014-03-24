# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

JENKINS_CI = ENV['JENKINS_CI'] ? true : false
DJANGO_PROJECT_NAME = "{{ project_name }}"
CHEF_JSON = {
  "build_essential" => {
    "compiletime" => true
  },
  "postgresql" => {
    "password" => {
      "postgres" => "vagrant"
    },
    "config" => {
      "client_encoding" => "UTF8",
      "default_transaction_isolation" => "read committed",
      "timezone" => "UTC"
    }
  },
  "twoscoops" => {
    "application_name" => DJANGO_PROJECT_NAME,
    "project_name" => DJANGO_PROJECT_NAME,
    "database" => {
      "engine" => "django.db.backends.postgresql_psycopg2",
       "username" => "postgres",
       "password" => "vagrant"
    }
  }
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu-12.04-omnibus-chef"
  config.vm.box_url = "http://grahamc.com/vagrant/ubuntu-12.04-omnibus-chef.box"

  if JENKINS_CI
    config.vm.network :forwarded_port, guest: 8080, host: rand(30000) + 1024
  else
    config.vm.network :forwarded_port, guest: 8080, host: 8080
  end

  config.ssh.forward_agent = true

  config.berkshelf.enabled = true
  config.omnibus.chef_version = :latest

  # DEFAULT BOX
  config.vm.define :default, primary: true do |default|
    default.vm.provision :chef_solo do |chef|
      chef.node_name = DJANGO_PROJECT_NAME
      chef.json = CHEF_JSON

      chef.run_list = [
        "build-essential",
        "postgresql::server",
        "python",
        "supervisor",
      ]

      chef.add_recipe JENKINS_CI ? "twoscoops::test" : "twoscoops::local"
    end
  end

end
