from os import getenv

from flask import Flask
from dotenv import load_dotenv

from strategies import KafkaWriter, ConsoleWriter

app = Flask(__name__)
load_dotenv()


@app.route('/', methods=['GET'])
def write():
    with open('/Users/daniiloleshchuk/University/SoftwareDocDesign/Lab4-py/text.txt', 'r+') as file:
        text = file.read()
    strategy = KafkaWriter if getenv('strategy') == 'kafka' else ConsoleWriter
    strategy.write(text=text)
    return {}, 200


if __name__ == '__main__':
    app.run(port=1234)
