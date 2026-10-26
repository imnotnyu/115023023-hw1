def medication_risk(age, dose_per_time, times_per_day):
    # Write your code here
    return "High" if (dose_per_time * times_per_day) > 50 or age >= 65 else "Normal"