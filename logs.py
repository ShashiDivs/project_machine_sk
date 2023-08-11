from flask import Flask
from src.logger import logging


app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    logging.info("we are Testing logging file")

    return "Welcome to Shashi"



if __name__ == "__main__":
    app.run(port=6000,debug=True)