Introvert_points = 0
Extrovert_points = 0
Ambivert_points = 0
print("Personality Quiz!!!")
input("")
answer1 = input("On a day off, what would you be doing: A, hanging out with friends B, sitting around at home or C either, just depends on the day")
if answer1 == "A":
    Extrovert_points += 1
elif answer1 == "B":
    Introvert_points += 1
elif answer1 == "C":
    Ambivert_points += 1
input("")
answer2 = input("How many friends overall do you have? A, 0-1 B, 1-3 C, 3-8 D, 8-15 F, 15-20 or E, 20+")
if answer2 == "A or B":
    Introvert_points += 1
elif answer2 == "C or D":
    Ambivert_points += 1
elif answer2 == "F or E":
    Extrovert_points += 1
input("")
answer3 = input("Do you, A, have a lot of friends but aren't super tight with most, B, have a few best friends and don't really talk to others, or C, have a mix of both")
if answer3 == "A":
    Extrovert_points += 1
    Ambivert_points += 1
elif answer3 == "B":
    Introvert_points += 1
elif answer3 == "C":
    Extrovert_points += 1
    Ambivert_points += 1
input("")
answer4 = input("Would you rather, A go to a big family gathering with people you love, B go over to a close friends house fo a few hours, or C stay at home all day")
if answer4 == "A" or answer4 == "a":
    Extrovert_points += 1
elif answer4 ==  "B":
    Ambivert_points += 1
elif answer4 == "C":
    Introvert_points += 1
input("")
answer5 = input("Do you feel A, energized after socializing, B, drained, or C no real reaction")
if answer5 == "A":
    Extrovert_points += 1
elif answer5 == "B":
    Introvert_points += 1
elif answer5 == "C":
    Ambivert_points += 1
input("")
print(f"Your score is {Extrovert_points} extrovert, {Introvert_points} introvert, and {Ambivert_points} ambivert")
input("")
if Extrovert_points >= Introvert_points and Extrovert_points >= Ambivert_points:
    print("You are definitely extroverted! You like hanging out with friends whenever you can and fined alone time boring!")
elif Introvert_points >= Extrovert_points and Introvert_points >= Ambivert_points:
    print("You are Introverted! You like having your own time, and would much rather be at home in peace and quiet then out and about")
elif Ambivert_points >= Extrovert_points and Ambivert_points >= Introvert_points:
    print("You are definitely an ambivert! What you do on any given day really just depends on who's available and what you feel up to!")