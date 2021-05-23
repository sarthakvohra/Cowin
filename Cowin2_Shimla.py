import requests
import json
import datetime
import time
import os
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=149&date=24-05-2021"
url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=149&date=13-05-2021"

blackList=["CHC Kupvi CVC", "PHC Jeori CVC", "CH NERWA CVC", "CHC Chirgaon CVC", "PHC Kholighat CVC"]
# blackList=""

def notInblacklist(name):
    for names in blackList:
        if name==names:
            return False
    return True

def get_data(districtCode, date, vaccine="*"):
    r=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+districtCode+"&date="+date,headers=headers)
    data=r.json()
    check=r.text
    centres=data["centers"]
        # centers=ses["name"]
    if (len(centres)>0):
        totalCentres=0
        for centre in centres:
            if notInblacklist(centre["name"]):
                ctr=0
                sessions = centre["sessions"]
                if vaccine!="*":
                    for ses in sessions:
                        if ses["available_capacity"]>0 and ses["vaccine"]==vaccine:
                            # data_all+=f'Date: {ses["date"]}\nVaccine: {ses["vaccine"]}\nMin Age: {ses["min_age_limit"]}\nCapacity: {ses["available_capacity"]}\n'
                            ctr+=1
                            totalCentres+=1
                    if ctr!=0:
                        print(f'\nCentre name: {centre["name"]}\nCentre address: {centre["address"]}')
                        sessions = centre["sessions"]
                    for ses in sessions:
                        if ses["available_capacity"]>0 and ses["vaccine"]==vaccine:
                            print(f'Date: {ses["date"]}\nVaccine: {ses["vaccine"]}\nMin Age: {ses["min_age_limit"]}\nCapacity: {ses["available_capacity"]}')
                else:
                    for ses in sessions:
                        if ses["available_capacity"]>0:
                            ctr+=1
                            totalCentres+=1
                    if ctr!=0:
                        print(f'\nCentre name: {centre["name"]}\nCentre address: {centre["address"]}')
                        sessions = centre["sessions"]
                    for ses in sessions:
                        if ses["available_capacity"]>0:
                            print(f'Date: {ses["date"]}\nVaccine: {ses["vaccine"]}\nMin Age: {ses["min_age_limit"]}\nCapacity: {ses["available_capacity"]}')
        # 	# data_all.append({"centre_name":centre["name"],"centre_address":centre["address"], "vaccine":centre["vaccine"],"minAge": centre["min_age_limit"]})
        if totalCentres==0:
            return False
        return True
    else:
        return False

x = datetime.datetime.now()
date=x.strftime("%d-%m-%Y")
while True:       #to let the program refresh every minute
    ctr=0
    x = datetime.datetime.now()
    date=x.strftime("%d-%m-%Y")
    for i in range(4):
        x+=datetime.timedelta(days=i*7)
        date=x.strftime("%d-%m-%Y")
        # if get_data("149", date)==False:    #for south delhi
        if get_data("208", date)==False:      #for gurgaon 208-shimla
            # print(f'Week {i+1}: No centre found')
            ctr+=1
    if ctr==4:
        print("No centre found")
    else:
        os.system('cmd /c "explorer "https://www.cowin.gov.in/home""') 
    time.sleep(120)

# get_data("149", "14-05-2021", "COVAXIN")
ctr=0                  #to run the program only once
for i in range(4):
    x+=datetime.timedelta(days=i*7)
    date=x.strftime("%d-%m-%Y")
    # if get_data("149", date)==False:    #for south delhi
    if get_data("208", date)==False:      #for gurgaon
        # print(f'Week {i+1}: No centre found')
        ctr+=1
if ctr==4:
    print("No centre found")
# print("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+"149"+"&date="+date)