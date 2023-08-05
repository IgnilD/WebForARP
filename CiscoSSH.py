import paramiko
import time


def show_command(commands, **router):
    ssh_client = paramiko.SSHClient()
    print(f"connecting to {router['hostname']}:{router['port']}")
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(**router)
    shell = ssh_client.invoke_shell()
    shell.send("terminal length 0\n")

    result = {}
    for command in commands:
        shell.send(f"{command}\n")
        time.sleep(1)
        output = shell.recv(10000)
        output = output.decode('utf-8')
        result[command] = output

    if ssh_client.get_transport().is_active():
        print("Closing connection")
        ssh_client.close()

    return result


router = {'hostname': '192.168.146.1',
          'port': '22',
          'username': 'python',
          'password': 'python',
          'look_for_keys': False,
          'allow_agent': False
          }

commands = ['sh ip int', 'sh ip arp']

with open(f"/home/alexandru/WebForARP_Work/cisco_ip_int_arp/{router['hostname']}_result.txt") as file:
    file.write(show_command(commands, **router))
