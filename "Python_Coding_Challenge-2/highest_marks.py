students = {"A":80,"B":95,"C":78}

top = ""
max_marks = 0

for key in students:
    if students[key] > max_marks:
        max_marks = students[key]
        top = key

print(top)