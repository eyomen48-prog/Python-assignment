students = [
    {"name": "Ali", "score": 78},
    {"name": "Ayşe", "score": 92},
    {"name": "Mehmet", "score": 88},

]
sirali = sorted(students, key=lambda s: (-s["score"], s["name"]))
print(sirali[0])