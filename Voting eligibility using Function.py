def check_vote(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not Eligible"

age = int(input("Enter Age: "))

result = check_vote(age)

print(result)