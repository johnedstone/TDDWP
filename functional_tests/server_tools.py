from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

# Right now, Fabric is only verified on python 2
# so wrapping this in subprocess
def create_session_on_server(host, email):
    ''' fab -i ~/.ssh/aws_superlist.pem deploy:host=ubuntu@superlist-staging.johnedstone-ec2.net'''
    return subprocess.check_output(
        [
            'fab',
            '-i',
            '~/.ssh/aws_superlist.pem',
            'create_session_on_server:email={}'.format(email),
            '--host=ubuntu@{}'.format(host),
            '--hide=everything,status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()

def reset_database(host):
    subprocess.check_call(
        ['fab',
         '-i',
         '~/.ssh/aws_superlist.pem',
         'reset_database',
         '--host=ubuntu@{}'.format(host),
         ],
        cwd=THIS_FOLDER
    )
# vim: ai et sts=4 ts=4 sw=4
