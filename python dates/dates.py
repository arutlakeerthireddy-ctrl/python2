#python Dates:A date in python is not a datatype of its own,but we can import a module named datetime to work with dates as dates objects
#example:
import datetime
x=datetime.datetime.now()
print(x)
#2026-05-26 22:18:10.365106

#creating date objects:to create date object we use datetime() class of the datetime module
#the datetime() requires three parameters to create date:year,month,day
#example:Create a date object
import datetime
x=datetime.datetime(2005,11,15)
print(x)#2005-11-15 00:00:00

#datetime() class also takes parameters for time and timezone(hour,minute,second,microsecond,tzone)

#The strftime() method:the datetime object has a method for formatting date objects into readable strings
#the method strftime() takes one parameter,format,to specify the format of returned string
#example:Display the name of the month:
import datetime
x=datetime.datetime(2005,11,15)
print(x.strftime("%B"))#November

#%a:weekday,short version
print(x.strftime("%a"))#Tue
#%A:weekday,full version
print(x.strftime("%A"))#Tuesday
#%w:weekday as number(0-6),0 is sunday
print(x.strftime("%w"))#2
#%d:day of month(1-31)
print(x.strftime("%d"))#15
#%b:month name,short version
print(x.strftime("%b"))#Nov
#%B:month name,full version
print(x.strftime("%B"))#November
#%m:month as number(01-12)
print(x.strftime("%m"))#11
#%y:year,short version
print(x.strftime("%y"))#05
#%Y:year,full version
print(x.strftime("%Y"))#2005
#%H;hour 00-23
print(x.strftime("%H"))#00
#%I:Houe 00-12
print(x.strftime("%I"))#12
#%p:AM/pM
print(x.strftime("%p"))#AM
#%M:minute 00-59
print(x.strftime("%M"))#00
#%S:second 00-59
print(x.strftime("%S"))#00
#%f:Microsecond 000000-999999
print(x.strftime("%f"))#000000
#%Z:Timezone
print(x.strftime("%Z"))
#%C:Century
print(x.strftime("%C"))#20
#%c:local version of date and time
print(x.strftime("%c"))#Tue Nov 15 00:00:00 2005
#%x:kocal version of date
print(x.strftime("%x"))#11/15/05
#%X:local version of time
print(x.strftime("%X"))#00:00:00
#%j:Day number of year 001-366
print(x.strftime("%j"))#319
#%U:week number of year,sunday as first day of week,00-53
print(x.strftime("%U"))#46
#%W:week number of year,monday as first day of week,00-53
print(x.strftime("%W"))#46