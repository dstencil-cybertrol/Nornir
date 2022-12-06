from distutils.command.config import config
import pathlib
from nornir import InitNornir
from nornir_utils.plugins.tasks.networking import tcp_ping
from nornir_utils.plugins.tasks import networking
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get



switch_name = str(input('Enter name of Device'))

nr = InitNornir(config_file="/root/nornir/inventory/config.yaml")

switch = nr.filter(name=switch_name)

result = switch.run(task=napalm_get, getters=['facts', 'interfaces_ip'])
)

print_result(result)
