hours = int (input ("Enter Hours:"))
rate = int (input ("Enter Rate:"))
if hours <= 40:
    pay = str (hours*rate)
    print ("Pay:" + pay)
else:
    newHours = hours - 40
    newRate = rate * 1.75
    pay = str (40 * rate + newHours*newRate)
    print ("Pay:" + pay)