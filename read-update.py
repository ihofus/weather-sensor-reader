# pylint: disable=C0111
import sys
import configparser
import requests

def post_data(temperature, humidity, url, api_key):
    form = {'api_key': api_key, 'field1': temperature, 'field2': humidity}
    resp = requests.post(url, data=form)
    print resp.status_code

def read_data(pin, sensor):
    #TODO read real sensor data
    return 44, 55

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

    print 'Posting... '
    post_data(temperature, humidity, url, api_key)


if __name__ == "__main__":
    CONFIG_FILE = 'configs.ini'
    if len(sys.argv) > 1:
        CONFIG_FILE = sys.argv[1]

    read_update_data(CONFIG_FILE)
