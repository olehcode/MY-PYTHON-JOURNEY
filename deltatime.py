#timedate.timedelta demostration
from datetime import datetime, timedelta 
date_inform = datetime.now() #creating a new variable with value of todays date and time
print("TODAYS INFO... ", date_inform) #printing todays date and time
future_2_years_date = date_inform + \
                      timedelta (days = 730) #creating a new variable that will contain a data of future, todays date + 2 years(365+365), also it will change automatically day
print("FUTURE INFO...", future_2_years_date)
