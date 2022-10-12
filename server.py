from flask import Flask, render_template, request

ip_info = ''
password = '123456789'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    global ip_info
    global password

    if request.method == 'GET':
        if ip_info == '':
            return 'have not any ip info!'
        else:
            return ip_info

    elif request.method == 'POST':
        client_password = request.form.get('password')
        if password == client_password:
            ip_info = request.form.get('ip_info')
            return 'update ip info success!'
        else:
            return 'password error!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=12345, use_debugger=False)