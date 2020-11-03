time = int(input("how many hours?:"))
while time>=13:
    print("this is a 12hour to 24 hour converter") 
    time = int(input("how many hours?:"))
minutes = int(input("how many minutes past?:"))
while minutes>59 :
    print("hey! minutes only go to 59!")
    minutes = int(input("how many minutes past?:"))
    
ampm = input("AM or PM?:")


if ampm == "PM":
    time+=12
    print(time,":", minutes)
if time in [1,2,3,4,5,6,7,8,9]:
    final = "0"+ str(time)
    if minutes in [1,2,3,4,5,6,7,8,9]:
        end = "0"+str(minutes)
    else:
        end=minutes
    print(final, ":",end)
elif time in [10,11,12]:
    if minutes in [1,2,3,4,5,6,7,8,9]:
        ok = "0"+str(minutes)
    print(time,":",ok)
