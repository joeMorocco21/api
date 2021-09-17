from flask import Flask, render_template, request, Response
from flask import jsonify
import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import os
class Apps():
    def predict(symbo,fType,asp,doo,carbody,drwh,enlo,whba,clength,cwidth,cheight,cuwe,enty,cynum,engsize,fsys,bratio,stroke,compRatio,hpower,prpm,cmpg,hmpg):
        model = pickle.load(open(os.path.join(os.path.dirname(__file__),'Pricing_prediction.pkl'), 'rb'))
        scalX = pickle.load(open(os.path.join(os.path.dirname(__file__),'ScalX.pkl'), 'rb'))
        scaly = pickle.load(open(os.path.join(os.path.dirname(__file__),'Scaly.pkl'), 'rb'))
        df = pd.read_csv(os.path.join(os.path.dirname(__file__),"cars.csv"))
        df
        dfl= df[['symboling',"fueltype","aspiration","doornumber","carbody","drivewheel","enginelocation","enginetype","cylindernumber","fuelsystem"]]
        symbo = 3
        result=[]
        for col,i in zip(dfl, dfl.columns):
            m = pd.Series([i])
            mu = pd.DataFrame(np.sort(dfl[col].unique()),columns=m)
            result.append(mu)
        result
        rs = result[0] == symbo
        rsv = rs.astype(int)
        ft = result[1] == fType
        ftyv = ft.astype(int)
        aspr = result[2] == asp
        asprv = aspr.astype(int)
        donum = result[3] == doo
        donumv = donum.astype(int)
        carBo = result[4] == carbody
        carBov = carBo.astype(int)
        driveW = result[5] == drwh
        driveWv = driveW.astype(int)
        enlocation = result[6] == enlo
        enloccationv = enlocation.astype(int)
        entype = result[7] == enty
        entypev = entype.astype(int)
        cyl = result[8] == cynum
        cylv = cyl.astype(int)
        fs = result[9] == fsys
        fsv = fs.astype(int)
        str = np.concatenate((rsv,ftyv,asprv,donumv,carBov,driveWv,enloccationv,entypev,cylv,fsv),axis=None)
        ft = list(str)
        ft
        cats = [elem for elem in ft]
        print(cats)
        cat = cats 
        num = [whba,clength,cwidth,cheight,cuwe,engsize,bratio,stroke,compRatio,hpower,prpm,cmpg,hmpg]  
        print(num)
        df_num = pd.Series(num)
        df_cat = pd.DataFrame(cat)
        numscal = pd.DataFrame(scalX.transform(df_num.values.reshape(1, -1)))
        #numscal = pd.DataFrame(scalX.transform(df_num.values))
        entree = pd.concat([df_cat.T, numscal],axis=1).values
        prop = model.predict(entree)
        Our_estimation = scaly.inverse_transform(prop[0]).round(2)
        print(Our_estimation)
        resp = pd.DataFrame(Our_estimation)
        if Our_estimation < 0:
            return render_template('index.html', prediction_text="Sorry !!!")
        else:
            return Response(resp.to_json(orient="records"), mimetype='application/json')

