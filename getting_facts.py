from distutils.command.config import config
import pathlib
from nornir import InitNornir
from nornir_utils.plugins.tasks.networking import tcp_ping
from nornir_utils.plugins.tasks import networking
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir_napalm.plugins.tasks import napalm_get
from datetime import date
import pathlib

def getting_facts(task):
    config_dir = "config-archive"
    device_dir= config_dir + "/" + task.host.name
    pathlib.Path(config_dir).mkdir(exist_ok=True)
    pathlib.Path(device_dir).mkdir(exist_ok=True)
    r = task.run(napalm_get, getters=["facts"])
    task.run(
        task=write_file,
        content=r.result["facts"]["os_version"],
        filename=f"{str(device_dir)}/facts_{str(date.today())}.txt"
    )

nr = InitNornir(config_file="/root/nornir/inventory/config.yaml")
result = nr.run(
    name="GATHERING DEVICE INFO", task=getting_facts
)

print_result(result)
