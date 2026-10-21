from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load dataset
df = pd.read_csv("house_data.csv")

# Features and target
X = df[['area', 'bedrooms', 'bathrooms']]
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    area = int(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])

    new_house = pd.DataFrame(
        [[area, bedrooms, bathrooms]],
        columns=['area', 'bedrooms', 'bathrooms']
    )

    prediction = model.predict(new_house)

    return render_template(
        'index.html',
        prediction_text=f"Predicted House Price: ₹ {prediction[0]:,.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)