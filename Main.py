import calendar as cl

# Calendar year:
yyyy = 2024

# Calendar month:
mm = 1

# Will start at day X and end at day Y:
start = 1
end = 5

skip = 1 # If you want to skip days, so 1 means every day will count, 2 means every other day will count, so 1-0-1-0-1-0, 3 means 1-0-0-1-0-0-1-0-0...
removeDays = [] # If you don't want to include some days in the count, like '6 - Saturday' or '7 - Sunday', Example: [6, 7]

# Code:
title = "     myCalendar" # I recommend you using spaces to center if you want to make it look better
allRemoveDays = []
monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i in range(1, 5):
    for day in removeDays:
        if day not in allRemoveDays:
            allRemoveDays.append(day)
        temp = day + (7 * i)
        if temp <= 31:
            allRemoveDays.append(temp)

print(f"Removed days: {allRemoveDays}\n")
calString = cl.month(yyyy, mm)
calString = calString.replace(f"    {cl.month_name[mm]} {yyyy}", f"{title}")

for i in range(start, end + 1, skip):
    if i not in allRemoveDays:
        if i >= 10:
            calString = calString.replace(f" {i} ", "  X ");
            calString = calString.replace(f"{i} ", " X ");
            calString = calString.replace(f" {i}", "  X ");
            calString = calString.replace(f"{i}", "  X ");
        elif i == 7:
            calString = calString.replace(" 7", " X ");
        else:
            calString = calString.replace(f" {i} ", " X ");


print(calString)