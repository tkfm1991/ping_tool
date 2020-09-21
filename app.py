from flask import Flask, render_template, redirect, url_for, request
#import hello
import ping
import pprint

app = Flask(__name__)


class Ping:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip


ping_list = [
    Ping('HostA', '192.168.10.1'),
    Ping('HostB', '192.168.10.102'),
    Ping('HostC', '192.168.10.104'),
    Ping('HostD', '192.168.10.105')
]


@app.route('/')
def top():
    return render_template('index.html', ping_list=ping_list)


@app.route('/summary')
def summary():
    return render_template('summary.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/get_ping')
def get_ping():
    ping_results = []
    print('process start')
    for host in ping_list:
        ping_results.append(ping.ping_cmd_args(host.ip))
        print(ping_results)

    print('process end')
    
    pprint.pprint(ping_results) 

    return render_template('index.html', ping_list=ping_list, ping_results=ping_results)

@app.errorhandler(404)
def redirect_main_page(error):
    return render_template(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0')
