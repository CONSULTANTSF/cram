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
(this will take a while - downloading from AWS)
(there may be ominous-looking errors but Vagrant migh be just fine - keep going)

### Install Python Libraries

```
vagrant ssh
```

```
cd /vagrant/
sudo pip install -r requirements.txt
```

If you get an error with pip (could be due to errors in instantiating Vagrant above), run 'sudo apt-get install python-pip' then repeat step above.

## Run Tests

```
vagrant ssh
```

```
cd /vagrant/
python -m pytest tests
```
