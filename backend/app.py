from flask import Flask, render_template

from usb_proxy import (get_usb_devices, ping)

app = Flask(__name__)


@app.route('/show_all_devices')
def all_devices():
    return render_template('all_devices.html', title='All devices', devices=get_usb_devices())


@app.route('/ping')
def pinger():
    return ping()


if __name__ == '__main__':
    app.run()
