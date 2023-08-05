import paramiko

router = {'hostname': '192.168.146.1',
          'port': '22',
          'username': 'python',
          'password': 'python',
          'look_for_keys': False,
          'allow_agent': False
          }

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(**router)
stdin, stdout, stderr = ssh.exec_command("ip arp print")
output = stdout.read().decode("ascii").strip("\n")

with open(f"/home/alexandru/WebForARP_Work/mikrotik_ip_int_arp/{router['hostname']}_result.txt", 'w') as f:
    f.write(output)

stdin, stdout, stderr = ssh.exec_command("ip address print")
output = stdout.read().decode("ascii").strip("\n")

with open(f"/home/alexandru/WebForARP_Work/mikrotik_ip_int_arp/{router['hostname']}_result.txt", 'a') as f:
    f.write(output)

ssh.close()
