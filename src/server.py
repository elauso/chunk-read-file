import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/read-file')
def read_file():
    
    filename = '/data/sample.csv'
    chunksize = 10 ** 6
    
    for chunk in pd.read_csv(filename, chunksize=chunksize):
        for index, row in chunk.iterrows():
            print(row)
    
    return 'ok'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)