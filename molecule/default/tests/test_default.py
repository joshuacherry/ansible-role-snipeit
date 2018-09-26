"""
Runs Default tests
Available Modules: http://testinfra.readthedocs.io/en/latest/modules.html

"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_snipeit_env_file(host):
    """
    Tests that the .env file exists and contains variables
    """
    variables = host.ansible.get_variables()
    hostname = variables["inventory_hostname"]
    file = host.file('/var/www/'+hostname+'/.env')

    assert file.exists
    assert file.user == 'www-data'
    assert file.group == 'www-data'


def test_apache2_is_installed(host):
    """
    Tests that apache2 is installed
    """
    apache2 = host.package("apache2")
    assert apache2.is_installed


def test_apache2_running_and_enabled(host):
    """
    Tests that apache2 is running and enabled
    """
    apache2 = host.service("apache2")
    assert apache2.is_running
    assert apache2.is_enabled


def test_apache2_80_is_listening(host):
    """
    Tests that apache2 is listening on ports 80
    """
    apache80 = host.socket("tcp://0.0.0.0:80")
    assert apache80.is_listening


def test_apache_request_status(host):
    """
    Tests that apache2 gives a 200 response
    """
    args = """url=http://127.0.0.1/setup
            follow_redirects=none validate_certs=no"""

    request = host.ansible("uri", args, check=False)
    assert request["status"] == 200
    assert request["server"] == "Apache"
