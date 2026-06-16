logs = [
    {"level": "INFO", "msg": "Started"},
    {"level": "ERROR", "msg": "DB connection failed"},
    {"level": "ERROR", "msg": "DB connection failed"},
    {"level": "WARN",  "msg": "Retrying"},
]
log = {"level": "ERROR", "msg": "DB connection failed"}
errors = [log for log in logs if log["level"] == "ERROR"]
print(errors)
frequency = {} 
for log in errors:
    mesaj = log["msg"]


    if mesaj in frequency:
        frequency[mesaj] = frequency[mesaj] + 1
    else:
        frequency[mesaj] = 1

print(frequency)
