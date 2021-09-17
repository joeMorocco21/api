import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pickle
import os
#raw = pd.read_csv(r'../Data/raw/cars.csv', encoding="UTF8")
raw = pd.read_csv(os.path.join(os.path.dirname(__file__),"cars.csv"))
#raw = raw[~raw['enginelocation'].str.contains('rear')].reset_index(drop=True)
'''raw = raw[(raw.cylindernumber != 'three') & (raw.cylindernumber != 'twelve')].reset_index(drop=True)
raw.loc[raw["CarName"].str.contains('diesel'), "fueltype"] = "diesel"
raw.loc[raw["CarName"].str.contains('turbo'), "aspiration"] = "turbo"
raw.loc[raw["CarName"].str.contains('"(sw)"'), "carbody"] = "wagon"
raw['enginetype'] = raw['enginetype'].replace({'dohcv':'dohc', 'ohcv': 'dohc', 'ohcf': 'dohc'})
raw['fuelsystem'] = raw['fuelsystem'].replace({'mfi':'mpfi', 'spfi': '2bbl'})

raw.drop(['enginelocation'], axis=1, inplace=True)'''
raw['symboling'] = raw['symboling'].astype('category')
for c in raw.columns:
    if raw[c].dtype == 'object': 
        raw[c] = raw[c].astype('category')

raw.drop(['car_ID'], axis=1, inplace=True)
raw.drop(['CarName'], axis=1, inplace=True)

clean=raw.copy()
clean_cat = clean.select_dtypes(include=['category'])
clean_num = clean.select_dtypes(exclude=['category'])
dummied_cat = pd.get_dummies(data=clean_cat, prefix=["sy", "ft", "as", "do", "ca", "dr", "el","et", "c", "fs"])

num_feat=clean_num.iloc[:,:-1]
price=clean_num.iloc[:,-1]

scalX = StandardScaler()
scalX = StandardScaler()

scalX.fit(num_feat.values)
scaly.fit(price.values.reshape(-1, 1))

df_features=pd.DataFrame(scalX.transform(num_feat.values))
target=pd.DataFrame(scaly.transform(price.values.reshape(-1, 1)))
data_input = pd.concat([dummied_cat, df_features], axis=1)

X = data_input.values
y = target.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
Price_prediction_model = LinearRegression(fit_intercept=True)
Price_prediction_model.fit(X_train, y_train)

with open(os.path.join(os.path.dirname(__file__),'Pricing_prediction.pkl'), 'wb') as file:
    pickle.dump(Price_prediction_model, file)
    
with open(os.path.join(os.path.dirname(__file__),'ScalX.pkl'), 'wb') as file:
    pickle.dump(scalX, file)

with open(os.path.join(os.path.dirname(__file__),'Scaly.pkl'), 'wb') as file:
    pickle.dump(scaly, file)