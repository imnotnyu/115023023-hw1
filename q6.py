def clinic_recommendation(age, systolic):
    # Write your code here
    return "Specialist" if systolic >= 140 or age >= 65 else "General"