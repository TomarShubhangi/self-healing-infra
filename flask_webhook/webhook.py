from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return 'Webhook is running!'

@app.route('/run-playbook', methods=['POST'])
def run_playbook():
    result = subprocess.call([
        '/usr/bin/ansible-playbook',   # use the output of `which ansible-playbook`
        '/home/ubuntu/self-healing-infra/ansible/playbooks/self_heal.yml',
        '-i',
        '/home/ubuntu/self-healing-infra/ansible/hosts.ini',
        '--private-key',
        '/home/ubuntu/self-healing-infra/app-node.pem'
    ])

    
    if result == 0:
        return 'Playbook executed successfully', 200
    else:
        return 'Playbook execution failed', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

