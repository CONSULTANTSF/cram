# Qbiz Training

## Installation and Setup

1. Install Vagrant.
2. Install VirtualBox.
3. Clone this Qbiz training repo.
4. Instantiate Vagrant VirtualBox

### Install Vagrant

[Instructions](https://www.vagrantup.com/docs/installation/) - [Downloads](https://www.vagrantup.com/downloads.html)

### Install VirtualBox

[Downloads](https://www.virtualbox.org/wiki/Downloads)

### Clone this Qbiz training repo

```
git clone git@github.com:Qbizinc/training.git
```

### Instantiate Vagrant VirtualBox

```
cd training
vagrant up
```

This will take a while. The following are happening:

1. If not already cached, download the Ubuntu VM image from AWS.
2. Initialize the VM from the image with the networking and storage mount options in the `Vagrantfile`.
3. Provision the VM using Ansible.

NB: There should be no errors, especially not Ansible errors. If there are, please reach out for help. The most common causes are:

* Networking configuration, especially on Windows.
* Transient network errors - "resolving" means DNS, etc.

### Install Python Libraries

```
vagrant ssh
```

```
cd /vagrant/
sudo pip install -r requirements.txt
```

If you get an error with `pip`, please reach out for help. `pip` should have been properly installed upon provisioning by the corresponding Ansible role.

## Run Tests

```
vagrant ssh
```

```
cd /vagrant/
python -m pytest tests
```
