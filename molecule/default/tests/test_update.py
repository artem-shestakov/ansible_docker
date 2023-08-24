import os
import pytest
import re
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.fixture()
def AnsibleFacts(host):
    facts = host.ansible("ansible.builtin.gather_facts")
    return facts['ansible_facts']

def test_update(host, AnsibleFacts):
    if AnsibleFacts['ansible_os_family'] == "RedHat":
        cmd = host.run("yum list docker-ce --showduplicates | sort -r | awk '{print $2}'")
    else:
        cmd = host.run("apt-cache madison docker-ce | awk '{ print $3 }'")
    result = re.match(r'\d:(\d+.\d+.\d+).*', cmd.stdout.split()[0])
    desired_version = result.group(1)
    cmd = host.run("docker -v")
    current_version = re.match(r'Docker version (\d+.\d+.\d+).*', cmd.stdout)
    assert desired_version == current_version.group(1)
