from flask import Flask
import urllib
import json

app = Flask(__name__)

@app.route('/show/<object>')
def show_price(object):
    str1 = 'You have entered ' + str(object)
    req = urllib.request.Request(
        'http://api.navasan.tech/latest/?api_key=freeNjvMdb6kkV8nEA9uLtHFwNAjcawo',
    data = None,
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    )
    response = urllib.request.urlopen(req)
    data = json.loads(response.read())
    #print(type(data))
    print(data)
    if object == 'gold':
        return '123$'
    elif object == 'oil':
        return '456$'
    else:
        return 'We don\'t have the price you entered'


if __name__ == '__main__':
    app.run()

