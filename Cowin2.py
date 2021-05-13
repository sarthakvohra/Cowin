import requests
import json
import time
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=149&date=24-05-2021"
url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=149&date=13-05-2021"



def get_data(districtCode,date, vaccine="*"):
    r=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+districtCode+"&date="+date,headers=headers)
    data=r.json()
    check=r.text
    centres=data["centers"]
        # centers=ses["name"]
    if (len(centres)>0):
        for centre in centres:
            # data_all=[]
            # print(f'\nCentre name: {centre["name"]}\nCentre address: {centre["address"]}')
            ctr=0
            sessions = centre["sessions"]
            if vaccine!="*":
                for ses in sessions:
                    if ses["available_capacity"]>0 and ses["vaccine"]==vaccine:
                        # data_all+=f'Date: {ses["date"]}\nVaccine: {ses["vaccine"]}\nMin Age: {ses["min_age_limit"]}\nCapacity: {ses["available_capacity"]}\n'
                        ctr+=1
                if ctr!=0:
                    print(f'\nCentre name: {centre["name"]}\nCentre address: {centre["address"]}')
                    sessions = centre["sessions"]
                for ses in sessions:
                    if ses["available_capacity"]>0 and ses["vaccine"]==vaccine:
                        print(f'Date: {ses["date"]}\nVaccine: {ses["vaccine"]}\nMin Age: {ses["min_age_limit"]}\nCapacity: {ses["available_capacity"]}')
            else:
                for ses in sessions:
                    if ses["available_capacity"]>0:
                        # print(f'Date: {ses["date"]}\nVaccine: {ses["vaccine"]}\nMin Age: {ses["min_age_limit"]}\nCapacity: {ses["available_capacity"]}')
                        ctr+=1
                if ctr!=0:
                    print(f'\nCentre name: {centre["name"]}\nCentre address: {centre["address"]}')
                    sessions = centre["sessions"]
                for ses in sessions:
                    if ses["available_capacity"]>0:
                        print(f'Date: {ses["date"]}\nVaccine: {ses["vaccine"]}\nMin Age: {ses["min_age_limit"]}\nCapacity: {ses["available_capacity"]}')
    
                # print('No vaccine available at the centre :(')

            # sessions=centre["name"]
            # for session in sessions:
            # if(vaccine!="*"):
            # 	if(centre["vaccine"]==vaccine):
            # 		print(f'Centre name: {centre["name"]}\nCentre address: {centre["address"]}\nVaccine: {centre["vaccine"]}\nMin Age: {centre["min_age_limit"]}')
            # else:
            # 	print(f'Centre name: {centre["name"]}\nCentre address: {centre["address"]}\nVaccine: {centre["vaccine"]}\nMin Age: {centre["min_age_limit"]}')
            # 	# data_all.append({"centre_name":centre["name"],"centre_address":centre["address"], "vaccine":centre["vaccine"],"minAge": centre["min_age_limit"]})
    else:
        print("No centre")


# print(get_data("188", "13-05-2021"))
# while True:
#     get_data("149", "13-05-2021", "COVAXIN")
#     time.sleep(20)
get_data("149", "24-05-2021", "COVAXIN")