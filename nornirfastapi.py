from fastapi import FastAPI
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from yaml import safe_load
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

nr = InitNornir(config_file="config/config.yaml")

app = FastAPI()


@app.get("/")
async def root():
    """Says hi!"""
    return {"message": "Hello JulioPDX"}


@app.get("/devices")
async def get_devices():
    """Returns a list of devices loaded from our hosts file"""
    with open("./config/hosts.yaml", encoding="utf-8") as file:
        devices = safe_load(file)
    return {"devices": devices}

@app.get("/devices/{hostname}/napalm_get/{getter}")
async def get_config(hostname: str, getter: str):
    """Function used to interact with NAPALM and devices"""
    rtr = nr.filter(name=f"{hostname}")
    return rtr.run(name=f"Get {hostname} {getter}", task=napalm_get, getters=[f"{getter}"])
  
  
  #Taken from: https://juliopdx.com/2021/09/01/integrating-nornir-with-fastapi/
