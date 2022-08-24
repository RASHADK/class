from datetime import date,timedelta
def all_sunday(year):
    dt=date(year,1,1)
   
    dt +=timedelta(days=6-dt.weekday())
    while dt.year==year:
        yield dt
        dt +=timedelta(days=7)
for s in all_sunday(2020):
    print(s)