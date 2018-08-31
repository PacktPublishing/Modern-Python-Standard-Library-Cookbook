import shlex
import subprocess

def run(command):
    try:
        result = subprocess.check_output(shlex.split(command),
                                         stderr=subprocess.STDOUT)
        return 0, result
    except subprocess.CalledProcessError as e:
        return e.returncode, e.output
for path in ('/', '/should_not_exist'):
    status, out = run('ls "{}"'.format(path))
    if status == 0:
        print('<Success>')
    else:
        print('<Error: {}>'.format(status))
    print(out)
