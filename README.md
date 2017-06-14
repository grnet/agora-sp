# Ansible playbooks for the Agora project

## Host requirements

The ansible-host machine should have pip installed, along with ansible installed from pip as well.

## Requirements

The only requirement is to have a Debian/Linux vm accessible with ssh.

First thing is that you should be sure that we have ssh access to the remote host(s). 

Edit the `hosts` file to provide the required information (such as the ip address of the server, the default user to connect).

## VM Requirements

Debian installations don't have python installed by default, so we will use the following command to install ansible dependencies:

```
ansible agora-ansible --sudo -m raw -a "apt-get install -y python python-simplejson"
```

## Provisioning

There are two basic playbooks that bootstrap the vm with the required packages and directories. You should run the following:

```
ansible-playbook playbooks/common.yml
ansible-playbook playbooks/agora.yml
```

## Cloning the repo
