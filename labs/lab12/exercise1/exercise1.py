correct_password = "python123"
attempts_used = 0
login_successful = False

for i in range (1,4):
    password =(input())
    attempts_used +=1

    if password == correct_password:
        login_successful = True 
        break

print(login_successful)
print(attempts_used)
