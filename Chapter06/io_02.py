with open('/var/log/install.log') as f:
    lines = list(f)

print(lines[:5])