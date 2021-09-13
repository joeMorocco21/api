from flask import Flask, render_template, jsonify, Response
import pandas as pd
from flask import request

app = Flask(__name__, template_folder='templates')
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result')
def result():
    return render_template('result.html')
df = pd.read_csv("C:\\Users\Joe\Desktop\py\melomane-flo_branch\olist\proCar\\app\cars.csv")
df.CarName = df.CarName.str.lower()
BrandName = df['CarName'].apply(lambda x : x.split(' ')[0])
ModelType = df['CarName'].apply(lambda x : ' '.join(x.split(' ')[1:]))
df.insert(3,"BrandName",BrandName)
df.insert(4,"ModelType",ModelType)
list_replace = [['alfa-romero', 'alfa romeo'], ['maxda', 'mazda'], ['porcshce', 'porsche'], ['toyouta', 'toyota'], ['vokswagen', 'volkswagen'], ['vw', 'volkswagen']]

for i in list_replace :
    df['BrandName'] = df['BrandName'].replace(i[0], i[1])
    dfBrand = df['BrandName'].unique()
    dfs = pd.DataFrame(dfBrand)
df_BrandModel = df[['BrandName', 'ModelType']]
df_BrandModel
@app.route('/cars')
def Brand():
    return Response(dfs.to_json(orient="records"), mimetype='application/json')
@app.route('/model/<terms>')
def model(terms):
    print(terms)
    resultats = df[df_BrandModel['BrandName']== terms]
    rs = resultats['ModelType'].unique() 
    dfm = pd.DataFrame(rs)
    return  Response(dfm.to_json(orient="records"), mimetype='application/json')
#if __name__ == "__main__":
 #   app.run()()