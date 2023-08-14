from datetime import datetime #importing module and class
now = datetime.now() #creating a variable now and asighning value of class datetime. and method now(), datetime.now() to know what time is it know 
t = now.strftime("%H:%M:%S:") #creatian a new variable t to imput data format(value) using ,method now(), and I write a needed format
print("Time in this format: ", t)#printing a value that is in a variable t
date_london= now.strftime("%d %m %y, %H:%M:%S:")#creating an new variable and asigning its value, the value of a newa variable is 2 methods now. and strftime().it will show us a time format in london
date_new_york= now.strftime("%m %d %y, %H:%M:%S:")#creating a new variable that will show un a time format in new york, we are creating a new variable and asighning value.
#I used method now. and method strftime to know what time it is and to asign a new format time 
print("London format: ", date_london)
print("New York format: ", date_new_york)
