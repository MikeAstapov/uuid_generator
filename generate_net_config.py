import configparser

config_file = configparser.ConfigParser()

config_file["Net_settings"] = {
    "port": "3000",
    "host": "127.0.0.1",


}

with open("net_settings.ini", 'w', encoding='utf-8') as file:
    config_file.write(file)
print("[INFO] Config file 'net_settings.ini' was created")

read_file = open('net_settings.ini')
content = read_file.read()
print(content)
