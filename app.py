from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.form

    gender = data["gender"]
    age = data["age"]
    profession = data["profession"]
    academic_pressure = data["academic_pressure"]
    work_pressure = data["work_pressure"]
    cgpa = data["cgpa"]
    study_satisfaction = data["study_satisfaction"]
    job_satisfaction = data["job_satisfaction"]
    sleep_duration = data["sleep_duration"]
    dietary_habits = data["dietary_habits"]
    degree = data["degree"]
    suicidal_thoughts = data["suicidal_thoughts"]
    work_study_hours = data["work_study_hours"]
    financial_stress = data["financial_stress"]
    family_history = data["family_history"]

    print("Gender :", gender)
    print("Age :", age)
    print("Profession :", profession)
    print("CGPA :", cgpa)

    return "Data received successfully"


if __name__ == "__main__":
    app.run(debug=True)
    