def is_eligible(age, citizenship, prison):

     
     if ((age >=18) and (citizenship == 'canadian' or citizenship == 'Canadian' or citizenship == 'Canada' or citizenship == 'canada')
           and (prison == 'no' or prison == 'No' or prison == 'NO')):
          return True
     else:
          return False
     
name=input("What is your name? ")
age= int(input("How old are you? "))
citizenship= input("what is your citizenship status? ")
prison= input("Are you convicted for a criminal offence: ")
if is_eligible(age, citizenship, prison):
     print(name, ", you are eligible to vote")
else:
     print(name, ", you are ineligible to vote") 
    



