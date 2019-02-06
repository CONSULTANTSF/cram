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

### 1.2. Relational Algebra

Relational algebra is a formal system of mathematics for reasoning about operations on a common data structure, tuplesets, which can informally be thought of as tables. Virtually all operations on data in contemporary analytics and data science are based on relational algebra.

We will learn, informally, how to think in terms of relational algebra. Don't worry, no theoretical math will be involved!

#### 1.2.1. Objectives

1. Learn what the primitive relational operators are and how to compose them.
2. Begin to understand how these operators may be implemented on concrete data types.
3. Start to develop a feel for the resource utilization of given relational operation execution trees.

#### 1.2.2. External Resources

1. http://infolab.stanford.edu/~ullman/fcdb/aut07/slides/ra.pdf
2. https://www.w3schools.in/dbms/relational-algebra/

#### 1.2.3. Internal Resources

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

1. Install a hypervisor - for Mac OSX we suggest Oracle VM VirtualBox (free and open-source); recent versions of Windows have a built-in hypervisor
2. Install Vagrant.
3. Clone this Qbiz training repo.
4. Instantiate Vagrant VirtualBox

#### 2.1.1. Install VirtualBox

[Downloads](https://www.virtualbox.org/wiki/Downloads)

#### 2.1.2. Install Vagrant

[Instructions](https://www.vagrantup.com/docs/installation/) - [Downloads](https://www.vagrantup.com/downloads.html)

#### 2.1.3. Clone This Qbiz Training Repo

```
git clone git@github.com:Qbizinc/training.git
```

#### 2.1.4. Instantiate Vagrant VirtualBox

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

#### 2.1.5. Install Python Libraries

```
vagrant ssh
```

```
cd /vagrant/
sudo pip install -r requirements.txt
```

If you get an error with `pip`, please reach out for help. `pip` should have been properly installed upon provisioning by the corresponding Ansible role.

### 2.2. Run Tests

```
vagrant ssh
```

```
cd /vagrant/
python -m pytest tests
```
