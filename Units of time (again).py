S = int(input("please print the total number of Seconds in the time duration"))

Seconds = S % 60    
Minutes = (S//60)
Hours = (Minutes//60)
Days = (Hours//24)
Minutes = (Minutes % 60)
Hours = (Hours % 24)

if (Seconds < 10):
    Seconds = str(Seconds)
    Seconds = "0" + Seconds 
if (Minutes < 10):
    Minutes = str(Minutes)
    Minutes = "0" + Minutes 
if (Hours < 10):
    Hours = str(Hours)
    Hours = "0" + Hours 
if (Days < 10):
    Days = str(Days)
    Days = "0" + Days

Seconds = str(Seconds)
Minutes = str(Minutes)
Hours = str(hours)
Days = str(Days)

print(Days + " " + "days" +" " + Hours + " " + "hours" + " " + Minutes " " + "minutes" + " " + Seconds + " " + "seconds")