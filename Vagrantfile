# Vagrantfile

Vagrant.configure("2") do |config|
  # Define the Vagrant box
  config.vm.box = "ubuntu/bionic64"

  # Give your VM a name
  config.vm.hostname = "api-db-nginx-vm"

  # Network settings, if needed
  config.vm.network "private_network", type: "dhcp"

  # Provisioning with a shell script to install dependencies
  config.vm.provision "shell", path: "provision.sh"

  # Forward ports if you need external access
  config.vm.network "forwarded_port", guest: 80, host: 8080

  # Sync folders, if needed (to access files on host machine)
  config.vm.synced_folder ".", "/vagrant"
end
