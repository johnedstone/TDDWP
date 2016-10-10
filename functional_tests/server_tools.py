from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

# Right now, Fabric is only verified on python 2
# so wrapping this in subprocess
def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'fab',
            'creat_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everything,status'
        ],
        cwd=THIS_FOLDER
    ).decode().strip()

def reset_database(host):
    subprocess.check_call(
        ['fab', 'reset_database', '--host={}'.format(host)],
        cwd=THIS_FOLDER
    )
