# Ansible playbooks for the Agora project

## Host requirements

The ansible-host machine should have `pip` installed, along with `ansible` installed from pip as well.

## Remote VM Requirements

The only requirement is to have a Debian/Linux vm accessible with ssh.

The first thing that you should be sure is that you have ssh access to the remote vm(s). 

## Prerequisites

Fist clone this repo:

```
git clone ssh://phab-vcs-user@phab.dev.grnet.gr:222/source/agora-ansible.git agora-ansible
```

and then cd into the ansible folder:

```
cd agora-ansible/ansible
```


You must configure the following variables in order for ansible to work correctly:

  - Inside `hosts` file, you should update the `<vm-ip>`, as shown below:

```
agora-ansible ansible_ssh_host=<vm-ip> ansible_ssh_user=root
```

  - Inside `group_vars/all` you should update the following:

```
...
repo_root: <local-agora-repo-root>
...
server_ip: <vm-ip>
...
admin_user: admin
admin_pass: test123456
admin_email: admin@vi-seem.eu

```

Where `<local-agora-repo-root>` is the git repository root directory of the `agora` repository. We will use the above repository to update the remote vm with the latest commit.

You can also change the default credentials of the django admin superuser, as shown above.

**NOTE**

You should whitelist the vm ip inside the `agora` codebase, as described in the `README.md` file of the `agora` project.

## Installation

Debian installations don't have python installed by default, so we will use the following command to install ansible dependencies:

```
ansible agora-ansible --sudo -m raw -a "apt-get install -y python python-simplejson"
```

From here you can run any playbook in order to install the desired configurations in the vm. 

Below is a brief explanation of all the playbooks inside the `playbooks` directory:

**The first 3 playbooks are the most important:**

### run_all.yml

With this playbook, everything will be installed automatically, and the project will be available on the `<vm-ip>` address. It includes all the roles:

  - common.yml
  - agora.yml
  - local.yml
  - deploy.yml
  - django.yml
  - django_admin.yml

It also restarts the apache2 service.

### bootstrap_machine.yml

This playbook prepares the whole environment for the code to be deployed. It aggregates the following roles:

  - common.yml
  - agora.yml

### deploy_code.yml

This playbook aggregates the roles required to take the latest commit of the `dev` branch, and deploy it in the vm, without touching the database. It also restarts the apache2 server. It aggregates the following roles:

  - local.yml
  - deploy.yml
  - django.yml

**The following roles are listed in the order of execution:**

### common.yml

This playbook bootstraps the environment of the vm, installing the required apt packages and setting default credentials for mysql.

### agora.yml

This playbook creates an empty directory for the code to be deployed inside and creates a mysql database named `agora`.

### git_prepare.yml

This playbook runs on your host machine, and it checks out the latest commit from the `dev` branch, and creates a `.tgz` file, ready to be deployed.

### deploy.yml

This playbook takes the `.tgz` file of the repo and sends it in the vm.

### django_admin.yml

This playbook creates a django admin superuser with default credentials.

```
admin_user: admin
admin_pass: test123456
admin_email: admin@vi-seem.eu

```

## Run

Just run `ansible-playbook playbooks/<playbook-name>` to run a playbook.

The default command to execute all is:

```
ansible-playbook playbooks/run_all.yml
```

In order to deliver a new version and update the codebase, run: 

```
ansible-playbook playbooks/deploy_code.yml
```