# employee years listed
years_list = [5, 7, 12, 13, 9, 21, 11, 10]
num_eligible = 0

# check all the employee 10-year anniversary eligibility
for i in years_list:
    if i > 9:
        num_eligible = num_eligible + 1
        print("colleague made 10 year anniversary: " + str(i) + " years")
print(str(num_eligible) + " made 10 year anniversary")
