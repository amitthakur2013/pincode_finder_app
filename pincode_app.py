import urllib.request, urllib.parse, urllib.error
import json
import ssl
from tkinter import *
root=Tk()
root.title('PinCode Finder')
root.geometry("540x340+0+0")
heading=Label(root,text="Welcome to Pincode Finder App",font=("arial",20,"bold"),fg="steelblue").pack()
label1=Label(root,text="Enter Location:",font=("serif",15,"bold"),fg="black").place(x=10,y=100)
name=StringVar()
entry_text=Entry(root,textvariable=name,width=25,bg="lightgreen").place(x=250,y=100)
label4=Label(root,text="eg. Haldia,WB").place(x=250,y=120)
label3 = Label(root, text="PinCode:", font=("serif", 18, "bold"), fg="black").place(x=10, y=220)

def do_it():
    api_key = False
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else:
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    address = str(name.get())

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)

    print(json.dumps(js, indent=4))

    l = len(js['results'][0]['address_components']) - 1


    try:
        pin = int(js['results'][0]['address_components'][l]['long_name'])

        label2=Label(root,text=str(pin),font=("serif",18,"bold"),fg="blue").place(x=250,y=220)
    except:
        label2 = Label(root, text="Sorry!Try more specific Location", font=("serif", 10, "bold"), fg="red").place(x=250, y=220)

work=Button(root,text="Find",font=("arial",10,"bold"),width=18,height=1,bg='lightblue',command=do_it).place(x=250,y=170)

root.mainloop()

