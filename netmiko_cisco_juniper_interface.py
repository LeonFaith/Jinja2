import json
from netmiko import ConnectHandler
import os 
from jinja2 import Environment, FileSystemLoader

device = { 
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
}

with ConnectHandler(**device) as net_connect:
    show_interface = net_connect.send_command("show ip interface brief", use_textfsm=True)


dir_name = "config_files"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory {dir_name} created.")
else:
    print(f"Directory {dir_name} already exists.")

file_name = "show_interface.json"
file_path = os.path.join(dir_name, file_name)

with open(file_path, 'w') as file: 
    json.dump(show_interface, file) 
    print(f"Interface information has been written to {file_path}")

# Convert the interface information to Juniper configuration
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('interface_config_cisco_juniper.j2')  # Replace with your template name

juniper_config = ''

for interface in show_interface:
    juniper_config += template.render(
        device_type='juniper',
        interface_name=interface['intf'],
        ip_address=interface['ipaddr'],
       # netmask=interface['netmask'],  # Ensure 'netmask' is available in your JSON data
       # description=interface['description']  # Ensure 'description' is available in your JSON data
    )

# Save the Juniper configuration into a file
juniper_file_name = "juniper_config.set"
juniper_file_path = os.path.join(dir_name, juniper_file_name)

with open(juniper_file_path, 'w') as file:
    file.write(juniper_config)

print(f"Juniper configuration has been written to {juniper_file_path}")

