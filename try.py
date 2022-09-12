import http.client
import json

#Function to search for train between Two station
def tsearch():

    a=input("Enter the startig station code")
    b=input("Enter the end station code")
    c='"GET", "/api/v2/trainBetweenStations?fromStationCode='+a+'&toStationCode='+b
    conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "b55efa6cefmsh1544a73b7a94ab9p13eb70jsn6846d2c4c550",
        'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
        }

    conn.request("GET", "/api/v2/trainBetweenStations?fromStationCode="+a+"&toStationCode="+b, headers=headers)

    res = conn.getresponse()
    data = res.read()

    e=json.loads(data.decode("utf-8"))
    print()
    print()
    print()

    
    for i in e["data"]:
        for j in i:
            print(j,i[j])
        print()
        print()
        print()
        print()
        print()
        print()
    print("Do you want to check seat aviliblity")
    ch2=input("Enter yes or no")
    if ch2=="yes" or ch2=="Yes" or ch2=="YES":
        seatcheck()
    else:
        print()

#Function for live train tracking
def ltsearch():

    conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")
    
    headers = {
        'X-RapidAPI-Key': "b55efa6cefmsh1544a73b7a94ab9p13eb70jsn6846d2c4c550",
        'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
        }
    
    conn.request("GET", "/api/v1/liveTrainStatus?trainNo=19038&startDay=1", headers=headers)

    res = conn.getresponse()
    data = res.read()
    
    print(data.decode("utf-8"))


def seatcheck():
    while True:
    
        classtype=input("Enter the class type ex-3A,2A,1A,SL")
        startst=input("Enter the starting station code ex-ADI")
        endst=input("Enter the end station code ex-BTH")
        quota=input("Enter the quota ex-GN,TQ,LD")
        date=input("Enter th date(yyyy-mm-dd) ex-2022-11-15")
        tnumber=input("Enter the train number for search")

        if classtype==1:
            break
        
    
    
        conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")
        
        headers = {
            'X-RapidAPI-Key': "b55efa6cefmsh1544a73b7a94ab9p13eb70jsn6846d2c4c550",
            'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
            }
        
        conn.request("GET", "/api/v1/checkSeatAvailability?classType="+classtype+"&fromStationCode="+startst+"&quota="+quota+"&toStationCode="+endst+"&trainNo="+tnumber+"&date="+date, headers=headers)
        
        res = conn.getresponse()
        data = res.read()
        
        print(data.decode("utf-8"))

    
        
    

while True:
    print("Welcome To The Program")
    print("1.To search train between station")
    print("2.Live train trackig")
    print("3.Exit")
    ch=int(input("Enter your choice"))

    if ch==1:
        tsearch()
        
    elif ch==2:
        ltsearch()
    elif ch==3:
        break







