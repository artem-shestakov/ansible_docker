# Ansible Docker role
Install Docker, Docker-compose and init Docker Swarm mode.

## Variables
| Title | Description |
| :---  | :---        |
| **advertise_iface** | Interface for swarm advertise. Default: default host interface (*ansible_default_ipv4.interface*)
| **advertise_addr** | Swarm advertised address. Default: the address of **advertise_iface**
| **docker_daemon_config** | Docker daemon configuration options. Use YAML format. Detail about options in [docs](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file).

## Example
Simple example to install Docker, Docker Compose and init Swarm mode
### Playbook
```yaml
---
- name: Install Docker and init Swarm
  hosts: swarm
  remote_user: vagrant
  become: true
  roles:
    - artem_shestakov.docker
  vars:
    - advertise_iface: eth1
```
### Inventory
```
[swarm]
swarm01 ansible_host=10.0.3.31 swarm_role=manager
swarm02 ansible_host=10.0.3.32 swarm_role=worker
swarm03 ansible_host=10.0.3.33 swarm_role=worker
```

### Vars
```yaml
vars:
  docker_daemon_config:
    data-root: "/docker"
    log-driver: "json-file"
    log-opts:
      max-file: "2"
      max-size: "100m"
```