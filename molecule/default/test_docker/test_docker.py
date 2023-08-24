import testinfra.utils.ansible_runner
import os


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_service(host):
    service = host.service("docker.service")
    assert service.is_enabled
    assert service.is_running

def test_docker_conf(host):
    docker_conf = host.file("/etc/docker/daemon.json")
    assert docker_conf.exists
    assert docker_conf.is_file
