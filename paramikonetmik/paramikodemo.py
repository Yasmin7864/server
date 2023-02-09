

import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.149.128",username="abdulyasmin",password="GAFFURasha@7")
#stdin,stdout,stderr=ssh.exec_command("ls -l")
stdin,stdout,stderr=ssh.exec_command("whoami")

'''pr="Permissions"
own="Owner"
usr="User"
sz="Size"
dt="Date"
nm="Name"
print("{0:8}{1:8}{2:8}{3:8}{4:8}{5}".format(pr,own,usr,sz,dt,nm))'''
for f in stdout:
    print(f)
stdout.close()


