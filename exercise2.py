import time #time module is imported 
t = time.strftime('%H:%M:%S') #variable 't' stores the current time 
print("The current time is " ,t)  #print the current time  


hour = int(time.strftime('%H'))  #variable 'hour' stores value of hour 
print(hour , "hours")  #print the hour

minute = int(time.strftime('%M'))   #variable 'minute' stores value of minute
print(minute , "minutes")    #print the minute

seconds = int(time.strftime('%S'))   #variable 'seconds' stores value of seconds
print(seconds , "seconds ")    #print the second

#check the condition
if(hour >= 0 and hour < 12):
    print("Message is : \"Good Morning Sir\"")
elif(hour >= 12 and hour < 17 ):
    print("Message is : \"Good Afternoon Sir\"")
elif(hour >=17  and hour < 0 ):
    print("Message is : \"Good night Sir\"")

#output :
#The current time is  15:30:47
#15 hours
#30 minutes
#47 seconds
#Message is : "Good Afternoon Sir"