date = str(input("Enter today's date: "))
date = date.strip()
mood = input("How do you rate your mood today froom 1 to 10? ")
thoughts = input("Let your thoughts flow:" + '\n')

with open(f"{date}.txt", 'w') as file:
    file_name = file.write(date + '\n')
    file.write(f"Your mood  {mood}" + 2*'\n')
    file.write(thoughts)
