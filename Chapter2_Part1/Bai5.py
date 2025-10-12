st = input("Enter your string: ")
first_five = st[:5]
last_five = st[-5:]
print("First five characters are:", first_five)
print("Last five characters are:", last_five)
print("Four strings of one line are:", 4 * (st + " "))
print("Four strings of four lines are:\n" + 4 * (st + "\n"))
