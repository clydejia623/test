
#coding=utf-8
import requests
import json

def get_city_code():
    citylist = {}
    try:
        with open("api_weather_cityid.json","r+") as fd:
            content = fd.readlines()
    except:
        print "open json file failed"
        return False
    for s in content:
        code = s[0:9]
        city = s[10:len(s)-1]
        citylist[city] = code
    return citylist
def get_weather_api(citycode = "101220101"):
    url = "http://www.weather.com.cn/data/cityinfo/%s.html" % (citycode)
    
    r = requests.get(url)
    
    #print r.status_code
    #print r.content
    r.encoding = 'utf-8'
    s = json.loads(r.text)
    
    print s['weatherinfo']['city'],':weather:',s['weatherinfo']['weather']
    print 'low temp:',s['weatherinfo']['temp1'],',high temp:',s['weatherinfo']['temp2']
    
    return s

if __name__ == "__main__":
    #get city code list
    citylist = get_city_code()
    #c = '合肥'
    #print citylist[c]
    
    #get weather
    r = get_weather_api(citylist['深圳'])
    
    