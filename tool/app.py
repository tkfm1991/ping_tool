from flask import Flask, render_template, url_for, request
from concurrent import futures

import datetime
#import hello
import ping
import pprint
import re

app = Flask(__name__)


class Ping:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip


host_list = [
    Ping('01_HostA', '192.168.10.1'),
    Ping('02_HostB', '192.168.10.102'),
    Ping('03_HostC', '192.168.10.104'),
    Ping('01_HostD', '192.168.10.105'),
    Ping('01_HostE', '192.168.10.112'),
    Ping('01_HostF', '192.168.10.113'),
    Ping('01_HostF', '192.168.10.113'),

]


@app.route('/')
def top():
    return render_template('index.html', host_list=host_list)


@app.route('/summary')
def summary():
    return render_template('summary.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/get_ping')
def get_ping():
    try:
        if request.method == 'GET':
            num = request.args.get('num', '')
            print(f'selected_num: {num}')
            #print(type(num))
    except Exception as e:
        return str(e)

    ping_list = select_host(host_list, num)

    print('process start')
    start_time = datetime.datetime.now()

    ping_results = single_thread(ping_list)

    print('process end')
    end_time = datetime.datetime.now()
    
    pprint.pprint(ping_results)
    total_time = end_time - start_time
    print(f'time: {total_time.seconds}')
    return render_template('index.html', host_list=host_list, ping_results=ping_results)


def single_thread(ping_list):
    ping_results = []
    for host in ping_list:
        ping_results.append(ping.ping_cmd_args(host.ip))
        #print(ping_results)

    return ping_results


def select_host(host_list, pattern):
    ping_list = []
    for host in host_list:
        if re.match(pattern, host.name):
            ping_list.append(host)
    
    return ping_list 


@app.route('/call_cli')
def clicall():
    try:
        if request.method == 'GET':
            host = request.args.get('host', '')
            print(f'clicall: {host}')
    except Exception as e:
        return str(e)

    ping_result = ping.ping_cmd_args(host)
    print('\n--- ping_result ---')
    pprint.pprint(ping_result)

    return render_template('index.html', host=host, ping_result=ping_result)


#@app.errorhandler(404)
#def redirect_main_page(error):
#    return render_template(url_for('top'))


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0')

