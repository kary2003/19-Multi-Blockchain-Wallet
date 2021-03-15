import subprocess
import json

command = './derive -g --mnemonic="clerk tongue ancient recall slush rival present legal play abstract water total acoustic surround genre" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
