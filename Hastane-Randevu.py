appointments = [
    {"doctor": "Dr. Can", "time": "09:00", "patient": "Ali"},
    {"doctor": "Dr. Can", "time": "10:30", "patient": "Ayşe"},
    {"doctor": "Dr. Ece", "time": "09:15", "patient": "Mehmet"},
]
grouped = {}
for appointment in appointments:
    grouped.setdefault(appointment["doctor"], []).append(appointment)
print(grouped)