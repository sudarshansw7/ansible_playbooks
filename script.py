import subprocess

i = 1
while i <= 4:
    subprocess.call("ansible-playbook playbook%d.yml -b"%i,shell=True)
    i = i + 1
