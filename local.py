import time

import helper
import requests

config = helper.read_config()
host = config["Api_settings"]["host"]
url = config["Api_settings"]["url"]
port = config["Api_settings"]["port"]

print()

start_time = time.time()

# for i in range(100):
res = requests.get(f"{host}{port}{url}")

print(res.text)

finish_time = time.time() - start_time
print(finish_time)
