from flask import Flask, render_template, request 
import joblib
import numpy as np
app = Flask(__name__)  
# Load the trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('my_scaler.save')
@app.route('/')
def home():
    return render_template("predict.html")
@app.route('/predict', methods=['POST'])   
def predict():   
    # Get the user input from the form
    try:
        pH = float(request.form['ph'])
        hardness = float(request.form['hardness'])  
        solids = float(request.form['solids'])
        chloramines = float(request.form['chloramines'])
        sulfate = float(request.form['sulphate'])
        conductivity = float(request.form['conductivity'])
        organic_carbon = float(request.form['organic_carbon'])
        trihalomethanes = float(request.form['Trihalomethanes'])
        turbidity = float(request.form['Turbidity'])

        # Prepare the input data for prediction
        input_data = np.array([[pH, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])

        # Scale the input data using the scaler used during training
        input_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_scaled)

        # Return the result
        if prediction == 1:
            result = "Safe Water Quality"
        else:
            result = "Unsafe Water Quality"
    except Exception as e:
        result = f"Error in input or prediction: {str(e)}"

    return render_template("predict.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
