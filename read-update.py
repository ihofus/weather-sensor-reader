# pylint: disable=C0111
#needs code from AdaFruit: https://github.com/adafruit/Adafruit_Python_DHT
import sys
import configparser
import requests
import Adafruit_DHT

def post_data(temperature, humidity, url, api_key):
    form = {'api_key': api_key, 'field1': temperature, 'field2': humidity}
    resp = requests.post(url, data=form)
    print resp.status_code

def read_data(pin, sensor):
    sensor_types = {'11': Adafruit_DHT.DHT11, '22': Adafruit_DHT.DHT22, '2302': Adafruit_DHT.AM2302}
    sensor_type = sensor_types[sensor]
    return Adafruit_DHT.read_retry(sensor_type, pin)

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def read_update_data(config_file):
    print 'Loading configs...'
    config = load_config(config_file)

    pin = config['GPIO']['pin']
    sensor = config['GPIO']['sensor']
    url = config['API']['url']
    api_key = config['API']['writeApiKey']

    print 'Reading sensor... '
    temperature, humidity = read_data(pin, sensor)

    if humidity is not None and temperature is not None:
        print 'Posting... '
        post_data(round(temperature, 2), round(humidity, 2), url, api_key)
    else:
        print 'Failed to read data.'

if __name__ == "__main__":
    CONFIG_FILE = 'configs.ini'
    if len(sys.argv) > 1:
        CONFIG_FILE = sys.argv[1]

    read_update_data(CONFIG_FILE)

