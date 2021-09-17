from flask import Flask, render_template, jsonify, Response
import pandas as pd
from flask import request
import os
from .apps import Apps
app = Flask(__name__, template_folder='templates')
    # Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
    # To get one variable, tape app.config['MY_VARIABLE']
class View(Apps):
    @app.route('/')
    def index():
        return render_template('index.html')
    @app.route('/result')
    def result():
        return render_template('result.html')
    @app.route('/cars')
    def Brand():
        df = pd.read_csv(os.path.join(os.path.dirname(__file__),"cars.csv"))
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
        return Response(dfs.to_json(orient="records"), mimetype='application/json')
    @app.route('/model/<terms>')
    def model(terms):
        print(terms)
        df = pd.read_csv(os.path.join(os.path.dirname(__file__),"cars.csv"))
        df.CarName = df.CarName.str.lower()
        BrandName = df['CarName'].apply(lambda x : x.split(' ')[0])
        ModelType = df['CarName'].apply(lambda x : ' '.join(x.split(' ')[1:]))
        df.insert(3,"BrandName",BrandName)
        df.insert(4,"ModelType",ModelType)
        list_replace = [['alfa-romero', 'alfa romeo'], ['maxda', 'mazda'], ['porcshce', 'porsche'], ['toyouta', 'toyota'], ['vokswagen', 'volkswagen'], ['vw', 'volkswagen']]
        for i in list_replace :
            df['BrandName'] = df['BrandName'].replace(i[0], i[1])
        df_BrandModel = df[['BrandName', 'ModelType']]
        df_BrandModel
        resultats = df[df_BrandModel['BrandName']== terms]
        rs = resultats['ModelType'].unique() 
        dfm = pd.DataFrame(rs)
        return  Response(dfm.to_json(orient="records"), mimetype='application/json')

    @app.route('/models/<symbo>/<fType>/<asp>/<doo>/<carbody>/<drwh>/<enlo>/<whba>/<clength>/<cwidth>/<cheight>/<cuwe>/<enty>/<cynum>/<engsize>/<fsys>/<bratio>/<stroke>/<compRatio>/<hpower>/<prpm>/<cmpg>/<hmpg>')
    def predicts(symbo,fType,asp,doo,carbody,drwh,enlo,whba,clength,cwidth,cheight,cuwe,enty,cynum,engsize,fsys,bratio,stroke,compRatio,hpower,prpm,cmpg,hmpg):
        return Apps.predict(symbo,fType,asp,doo,carbody,drwh,enlo,whba,clength,cwidth,cheight,cuwe,enty,cynum,engsize,fsys,bratio,stroke,compRatio,hpower,prpm,cmpg,hmpg)
        
    #if __name__ == "__main__":
    #   app.run()