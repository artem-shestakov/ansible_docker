# Ansible Docker role
Install Docker, Docker-compose and init Docker Swarm mode.

## Variables
| Title | Description |
| :---  | :---        |
| **advertise_iface** | Interface for swarm advertise. Default: default host interface (*ansible_default_ipv4.interface*)
| **advertise_addr** | Swarm advertised address. Default: the address of **advertise_iface**
