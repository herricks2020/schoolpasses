# we can run this through java or ruby, as in take the output list system from the gmail accounts, and account for it.

first = input('First Name: ')
last = input('Last Name: ')

first = first[:1].upper()
if len(last) <= 4:
elif len(last) > 4:  
  last = last[:3].lower()     //changed it to accomodate last name

for month in range(1,13):
  for date in range(1,32):
    for id in range(0,100):
      if id<10:
        id = '0' + str(id)
      print(first+last+str(month)+str(date)+str(id))
finalpass = first+last+number

//integration of ruby on rails as a usage for getting birthdates from FB. After that, we can determine the possible 100 numbers for testing.
