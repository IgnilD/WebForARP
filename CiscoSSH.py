import paramiko
import time


def show_command(commands, **router):
    ssh_client = paramiko.SSHClient()
    print(f"connecting to {router['hostname']}:{router['port']}")
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(**router)
    shell = ssh_client.invoke_shell()
    shell.send("terminal length 0\n".encode("bytes"))

    result = {}
    for command in commands:
        shell.send(f"{command}\n".encode("bytes"))
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

print(show_command(commands, **router))

# with open(file=f"{router['hostname']}_result.txt", mode="w") as file:
#     file.write(show_command(commands, **router))
