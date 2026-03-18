def can_vote(age):
    return age >= 18

age = int(input("Enter Age: "))

if can_vote(age):
    print("Eligible")
else:
    print("Not Eligible")