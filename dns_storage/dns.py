import re
import subprocess

def check_domain(domain):
    res = subprocess.run(f'dig any {domain} @ns2.mysterious-delivery.thecatch.cz'.split(), capture_output=True)

    txt = None
    for line in res.stdout.decode().splitlines():
        nsec_match = re.search('IN\s+NSEC\s+([^ ]*)', line)
        if nsec_match:
            nsec = nsec_match.group(1)

        txt_match = re.search('IN\s+TXT\s+(.*)', line)
        if txt_match:
            txt = txt_match.group(1)

    print(nsec, txt)
    return nsec


domain = 'mysterious-delivery.tcc'
while(True):
    domain = check_domain(domain)
