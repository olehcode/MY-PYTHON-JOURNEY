import datetime
now = datetime.datetime.now()
print("TODAY IS: ", now)

"""I can use 2 methods of printing data #1:
import datetime
now = datetime.datetime.now()
print("TODAY IS: ", now)
#2 from datetime import datetime
now= datetime.now()
print("TODAY IS: ", now)

!!!FOR ONLY DATE WE USE!!! datetime.date.today() ///
FOR DATE AND TIME WE USE!!! datetime.datetime.now()



from datetime import datetime 
module_=datetime.today()
print(module_)

from datetime import datetime 
module_=datetime.now()
print(module_)

!!!SAME RESULT!!!


from datetime import date // here we are using module datetime and importing class date
date1 = date(2023,10,19)
print(date1)


"""
