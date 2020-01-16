# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network :forwarded_port, guest: 8000, host: 8000
  
  config.vm.provision :shell, path: "vagrant/bootstrap.sh"
  
  config.trigger.after [:provision] do |t|
	  t.name = "Reboot after provisioning"
	  t.run = { :inline => "vagrant reload" }
  end
  
  config.vm.provider "virtualbox" do |v|
    v.name = "django_blog"
    v.memory = 1024 * 2
    v.cpus = 1
    v.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
  end
end
