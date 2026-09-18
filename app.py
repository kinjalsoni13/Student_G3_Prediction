from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("student_grade_model.pkl")

# Load the exact feature names used during training
feature_names = joblib.load("student_grade_features.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from website form
    age = int(request.form["age"])
    sex = request.form["sex"]
    school = request.form["school"]
    studytime = int(request.form["studytime"])
    failures = int(request.form["failures"])
    absences = int(request.form["absences"])
    G1 = int(request.form["G1"])
    G2 = int(request.form["G2"])

    # Create input data
    data = {
        "age": age,
        "studytime": studytime,
        "failures": failures,
        "absences": absences,
        "G1": G1,
        "G2": G2
    }

    # Add categorical values
    if sex == "M":
        data["sex_M"] = 1

    if school == "MS":
        data["school_MS"] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([data])

    # Make sure columns exactly match training features
    input_df = input_df.reindex(columns=feature_names, fill_value=0)

    # Prediction
    prediction = model.predict(input_df)[0]

    prediction = round(prediction, 2)

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)