from Basic_programs.agecalc import Agecalc
from Basic_programs.myexception import AgeException

age = int(input("Enter your age: "))

age_obj = Agecalc()

try:
    age_obj.voting_age_check(age)
    age_obj.pension_age_check(age)
except AgeException as e:
    print(e)

else:
    print("Eligible, Move to next step!!")