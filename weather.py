import urllib.parse
import urllib.request
import json
from flask import Flask, render_template, request, abort
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)

API_key=os.environ.get('API')

@app.route('/forecast', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city is None:
        abort(400, 'Missing argument city')
    data = {}
    data['q'] = request.args.get('city')
    data['appid'] = API_key
    data['units'] = 'metric'
    url_values = urllib.parse.urlencode(data)
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    full_url = url + '?' + url_values
    data = urllib.request.urlopen(full_url).read().decode('utf8')
    return render_template('index.html', title='Weather App', data=json.loads(data))

if __name__ == '__main__':
    app.run(debug=True)