def patient_risk(age, temperature):
    # Write your code here
    return "High" if temperature >= 38 or age >= 65 else "Low"