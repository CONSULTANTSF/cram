# Qbiz Training

## Table of Contents

1. Curriculum
   1. Scripting (with Python)
   2. Relational Algebra
   3. SQL
   4. MapReduce (with Hadoop)
   5. Lazy Distributed Data (with Spark)
   6. Orchestration of Data Tasks (with Airflow)
   7. Software Engineering (with Python)
2. Training Framework

## 1. Curriculum

### 1.1. Scripting (with Python)

"Scripting" implies:

- Orchestrating "real, engineered" software components to perform tasks.
- Ran as source code directly in an interpreter, skipping a compilation step.

Python was originally developed to be a pure scripting language. We will learn to script with Python.

#### 1.1.1. Objectives

1. Learn to write Python scripts to orchestrate other software components to perform tasks.
2. Begin to understand how to manage a Python interpreter in a particular operating system and environment.

#### 1.1.2. External Resources

1. https://www.udemy.com/the-python-bible/
2. https://developers.google.com/edu/python/
3. https://learnpythonthehardway.org/book/ (up to exercise 39)

#### 1.1.3. Internal Resources

### 1.3. SQL

#### 1.3.1. Objectives

#### 1.3.2. External Resources

1. https://www.w3schools.com/sql/
2. https://cs.ulb.ac.be/public/_media/teaching/infoh417/sql2alg_eng.pdf

#### 1.3.3. Internal Resources

### 1.4. MapReduce (with Hadoop)

#### 1.4.1. Objectives

#### 1.4.2. External Resources

1. https://pythonhosted.org/mrjob/guides/quickstart.html
2. https://www.tutorialspoint.com/map_reduce/
3. https://www.slideshare.net/shrihari2806/join-algorithms-in-mapreduce
4. https://www.slideshare.net/shalishvj/map-reduce-joins-31519757

#### 1.4.3. Internal Resources

### 1.5. Lazy Distributed Data (with Spark)

#### 1.5.1. Objectives

#### 1.5.2. External Resources

#### 1.5.3. Internal Resources

### 1.6. Orchestration of Data Tasks (with Airflow)

#### 1.6.1. Objectives

#### 1.6.2. External Resources

#### 1.6.3. Internal Resources

### 1.7. Software Engineering (with Python)

#### 1.7.1. Objectives

#### 1.7.2. External Resources

1. https://www.udemy.com/python-the-complete-python-developer-course/
2. https://learnpythonthehardway.org/book/

#### 1.7.3. Internal Resources

## 2. Training Framework

### 2.1. Installation and Setup

1. Install a virtualization host
   - For macOS and Linux, please use Oracle VM VirtualBox (free and open-source)
   - Windows 10 has a built-in hypervisor, enable Hyper V under Windows features
2. Install Vagrant.
3. Clone this Qbiz training repo.
4. Instantiate Vagrant
5. Install Python Libraries
6. Migrate the PostgreSQL Database

#### 2.1.1. Install VirtualBox

[Downloads](https://www.virtualbox.org/wiki/Downloads)

#### 2.1.2. Install Vagrant

[Instructions](https://www.vagrantup.com/docs/installation/) - [Downloads](https://www.vagrantup.com/downloads.html)

#### 2.1.3. Clone This Qbiz Training Repo

```
git clone git@github.com:Qbizinc/training.git
```

#### 2.1.4. Instantiate Vagrant

```
cd training
vagrant up
```

This will take a while. The following are happening:

1. If not already cached, download the Ubuntu VM image from AWS.
2. Initialize the VM from the image with the networking and storage mount options in the `Vagrantfile`.
3. Provision the VM using Ansible.

NB: On Windows and Linux, there can be transient DNS errors - "failed to resolve ...". Try the following up to 3 times with one minute gap.

```
vagrant provision
```

If the problem persists, please reach out for help.

#### 2.1.5. Install Python Libraries

```
vagrant ssh
```

```
cd /vagrant/
sudo pip install -r requirements.txt
```

If you get an error with `pip`, please reach out for help. `pip` should have been properly installed upon provisioning by the corresponding Ansible role.

#### 2.1.6. Migrate the PostgreSQL Database

```
alembic upgrade head
```

### 2.2. Run Tests

```
vagrant ssh
```

```
cd /vagrant/
python -m pytest tests
```
