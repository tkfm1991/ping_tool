import subprocess


def main():
    ping_cmd()

def ping_cmd():
    result = subprocess.run('ping -c 4 192.168.10.1', shell=True, stdout=subprocess.PIPE)
    result_str = result.stdout.decode()
    output = result_str.split('\n')
    return output


def ping_cmd_args(ip):
    cmd = 'ping -c 10 ' + ip
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    result_str = result.stdout.decode()
    output = result_str.split('\n')
    return output


if __name__ == '__main__':
    main()
