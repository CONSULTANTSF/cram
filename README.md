# Qbiz Training

## Installation and Setup

1. Clone this.
2. Install Vagrant.
3. Install VirtualBox.
4. Instantiate Vagrant VirtualBox

### Clone This

```
git clone git@github.com/qbizinc/training
```

### Install Vagrant

[Instructions](https://www.vagrantup.com/docs/installation/) - [Downloads](https://www.vagrantup.com/downloads.html)

### Install VirtualBox

[Downloads](https://www.virtualbox.org/wiki/Downloads)

### Instantiate Vagrant VirtualBox

```
vagrant up
```

### Install Python Libraries

```
vagrant ssh
```

```
cd /vagrant/
sudo pip install -r requirements.txt
```

## Run Tests

```
vagrant ssh
```

```
cd /vagrant/
python -m pytest tests
```
