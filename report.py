name = input("Write your full name: ")
age = input("How old are you? ")
score = input("How much do you get on the exam? ")

print(f"Hi, {name}.")
print(f"{name}, you are {age} years old and get {score} in the exam.")

if int(score) >= 70:
    print("You are approved!")
else:
    print("Not approved.")