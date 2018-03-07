from urllib2 import Request, urlopen, URLError

print('Enter ZIP Code:')
ZIP = input()
request = Request('http://api.openweathermap.org/data/2.5/weather?zip='+str(ZIP)+',us&appid=22fad0cc433054de7fa6fe22dcd2b5f9')

try:
    response = urlopen(request)
    weather = response.read()
except URLError, e:
    print 'Error', e

tempK = weather[weather.index("temp")+6:weather.index("temp")+12]
tempF = 1.8 * (float(tempK) - 273) + 32
print "The temperature at that location is "+str(tempF)+" degrees Fahrenheit."

if(tempF>=73.4):
    print "It is HOT (>=73.4)"
    host = 'https://api.yelp.com'
    search = '/v3/businesses/search'
    key = 'EVfllif2av6cSnIipleMTTNh4UKudxAyVr69DL3aQbW_5BREl1TinQFKligE9OdhAgxq82ddYrPPNdp-Yx0N_r3WiRorrcFYBID2NZ9XTrxGyfoe0taa5Xhmvm-fWnYx'
else:
    print "It is COLD (<73.4)"
    
