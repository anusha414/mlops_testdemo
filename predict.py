import joblib

model = joblib.load("student_pass_model.pkl")

hours = [[6]]

result = model.predict(hours)

if result[0] == 1:
    print("Student is likely to PASS")
else:
    print("Student is likely to FAIL")
