# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/xenial64"

  config.vm.network "forwarded_port", host_ip:"127.0.0.1", guest: 8080, host: 8080

  config.vm.provision "shell", inline: <<-SHELL

  sudo apt-get update
  sudo apt-get -y upgrade

  sudo locale-gen en_US.UTF-8

  sudo apt-get install -y python3-dev python3-pip

  sudo apt-get install -y libpq-dev postgresql postgresql-contrib

  pip install --upgrade pip
  pip3 install django djangorestframework djangorestframework-jwt psycopg2

  sudo pip3 install virtualenvwrapper
    if ! grep -q VIRTUAL_ALREADY_ADDED /home/ubuntu/.bashrc; then
      echo "# VIRTUAL_ALREADY_ADDED" >> /home/ubuntu/.bashrc
      echo "#WORKON_HOME=~/.virtualenvs" >> /home/ubuntu/.bashrc
      echo "PROJECT_HOME=/vagrant" >> /home/ubuntu/.bashrc
      echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/ubuntu/.bashrc
    fi

  # Postgre SQL

  SHELL
end
