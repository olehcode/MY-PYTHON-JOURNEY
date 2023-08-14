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


from datetime import datetime, date,timedelta
#only prints date(year,month, time)
a = date(year=2023,month=1,day=1)
b = date(year=2030,month=1,day=1)
c= a-b
print(c)
print("next method. using module datetime")
q= datetime(2023,10,10,3,3,1)
r= datetime(2025,5,4,2,1,3)
x=q-r;
print(x)

"""
