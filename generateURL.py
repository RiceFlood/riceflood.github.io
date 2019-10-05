# import simplegui 

def generateURL(sensor, date, days_past):
	url = 'https://api.thingspeak.com/channels/'
	#dayspastparsing
	roll_month = 0
	year, month, day = map(int, date.split('-'))
	fail = 0
	check = 0
	while((day+int(days_past))>28 and fail < 4):
	    check = 1
	    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
	        if(int(day) + int(days_past) > 31):
	            day = int(day) + int(days_past)
	            days_past = 0
	            #print('31 boy')
	    
	            roll_month = int(month)+1
	            if(roll_month<10):
	                month = (roll_month)
	            elif(roll_month==13):
	                month = '01'
	                year = str(int(year)+1)
	            else:
	                month = (roll_month)
	            print(month)
	            day = (int(days_past)+int(day) - 31)
	            #days_past = (int(days_past) - 31)
	            if(day<10):
	                str_day = '0' + str(day)
	            else:
	                str_day = str(day)
	            print(day)
	            fail = 0
	    if(month == 4 or month == 6 or month == 9 or month == 11):

	        if(int(day) + int(days_past) > 30): 
	            day = int(day) + int(days_past)
	            days_past = 0
	            #print('30 boy')

	            roll_month = int(month)+1
	            if(roll_month<10):
	                month =(roll_month)
	            else:
	                month = (roll_month)
	            print(month)
	            day = (int(days_past)+int(day) - 30)
	            #days_past = (int(days_past) - 30)
	            if(day<10):
	                str_day = '0' + str(day)
	            else:
	                str_day = str(day)
	            print(str_day)
	            fail = 0
	    if(month == 2):
	        if(int(day) + int(days_past) > 28): 
	            day = int(days_past) + int(day)
	            days_past = 0
	            #print('Feb')
	            month = 3
	            print(month)
	            day = (int(days_past)+int(day) - 28)
	            if(day<10):
	                str_day = '0' + str(day)
	            else:
	                str_day = str(day)
	            print(str_day)
	            fail = 0
	    fail = fail + 1

	if(check == 0):
	    day = day + int(days_past)
	    
	if(day < 10):
	    str_day = '0' + str(day)
	else:
	    str_day = str(day)
	if(month<10):
	    str_month = '0' + str(month)
	else:
	    str_month = str(month)
	end_date = str(year) + "-" + str_month +"-" + str_day

	#Add channel numbers here
	channels = dict({
	    "1": "824825",
	    "2": "824835",
	    "3": "824849",
	    "4": "824853",
	    "5": "842071",
	    "6": "842072",
	    "7": "842073",
	    "8": "842074"
	})

	#Add READ API keys here
	api = dict({
	    "1": "D2C6ZRLUY4RYOS2V",
	    "2": "U8LLWGVU0UIO9C9V",
	    "3": "9BNF3MHPLN39MCDB",
	    "4": "BOV93BV4CPEUOVWX",
	    "5": "NR3KNWN07B7PU7PJ",
	    "6": "OKMCXRC6884OKMPC",
	    "7": "4PAELGVIXKM0GMN8",
	    "8": "H37G5UKC6OCK0NI4"
	})
	#"2019-07-22"

	#Generating URL
	url2 = url+channels.get(sensor)
	url2 = url2 + "/charts/1?api_key="
	url2 = url2 + api.get(sensor) + "&"
	url2 = url2 + "start=" + date + "%2005:00:00&end="+end_date + "%2005:00:00&width=1600&step=true&dynamic=true&update=5"
	return url2

print(generateURL('1','2019-08-14','2'))