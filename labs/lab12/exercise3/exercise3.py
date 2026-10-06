grade = float(input())
valid_count=0
total_score = 0.0
while grade != -1:
    if grade <0 or grade >100:
        grade = float(input())
        continue

    valid_count +=1
    total_score+=grade
    grade = float(input())

if valid_count >0:
    average = total_score/valid_count
else:
    average = 0.0


print(valid_count)
print(f"{average:.2f}")
