from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and preprocessors
model_data = joblib.load("model.pkl")
model = model_data["model"]
preprocessor = model_data["preprocessor"]
scaler = model_data["scaler"]
encoded_cols = model_data["encoded_cols"]  # This should be ALL encoded columns
numeric_cols = model_data["numeric_cols"] # Not using this

# Only these are scaled. Important to use the transformed column names!
scaled_cols = ["age", "avg_glucose_level", "bmi"] # Original cols

def predict_input(user_input):
    input_df = pd.DataFrame([user_input])

    # Map gender
    input_df["gender"] = input_df["gender"].map({"Male": 0, "Female": 1})

    # Preprocess (encode + transform)
    transformed = preprocessor.transform(input_df)

    # Convert sparse matrix to dense if needed
    if hasattr(transformed, "toarray"):
        transformed = transformed.toarray()

    # Build dataframe with ALL encoded feature names, adding 'remainder__'
    encoded_df = pd.DataFrame(transformed, columns=encoded_cols)

    # Scale ONLY the numeric features, using correctly named columns
    scaled_cols_with_prefix = [f"remainder__{col}" for col in scaled_cols]
    encoded_df[scaled_cols_with_prefix] = scaler.transform(encoded_df[scaled_cols_with_prefix])

    # Final input to model
    prediction = model.predict(encoded_df)
    return prediction

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        gender = request.form["gender"].capitalize()
        age = int(request.form["age"])
        hypertension = int(request.form["hypertension"])
        heart_disease = int(request.form["heart_disease"])
        ever_married = request.form["ever_married"].capitalize()
        work_type = request.form["work_type"].title()
        residence_type = request.form["residence_type"]
        avg_glucose_level = float(request.form["avg_glucose_level"])
        bmi = float(request.form["bmi"])
        smoking_status = request.form["smoking_status"].lower()

        # Normalize work_type
        work_type_mapping = {
            "Government Job": "Govt_job",
            "Children": "children",
            "Never Worked": "Never_worked",
            "Private": "Private",
            "Self-Employed": "Self-employed"
        }

        single_input = {
            "gender": gender,
            "age": age,
            "hypertension": hypertension,
            "heart_disease": heart_disease,
            "ever_married": ever_married,
            "work_type": work_type_mapping.get(work_type, work_type),
            "Residence_type": residence_type,
            "avg_glucose_level": avg_glucose_level,
            "bmi": bmi,
            "smoking_status": smoking_status
        }

        prediction = predict_input(single_input)
        result = "🧠 Likely to have a stroke" if prediction[0] == 1 else "✅ Not likely to have a stroke"
        return render_template("result.html", result=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

