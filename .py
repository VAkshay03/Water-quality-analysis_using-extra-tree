from flask import flask,request,render_template
import pickle
import pandas as pd
import numpy as np
import joblib
scaler = joblib.load("ay_scaler.save")
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route("/home")
@app.route("/")
def hello():
    return render_template("predict.html") 
@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method=="POST":
        input_features=[float(x) for x in request.form.values()]
        features_value=[np.array(input_features)]
        features_names=["ph","Hardness","solids","chloramines","sulphate","conductivity","oraganic_carbon","Trihalomethanes","Turbidity"]
        df=pd.Frame(features_value,columns=features_names)
        df=scaler.transform(df)
        output=model.predict(df)
        if output[0]==1:
            prediction="safe"
        else:
            prediction="not safe"
        return render_template('predict.html',prediction_text="water id {} for human consumption".format(prediction))
if __name__ == "__main__":
    app.run(debug=True)
