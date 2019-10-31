def check_internet():
    try:
        import httplib
    except ImportError:
        import http.client as httplib

    conn = httplib.HTTPConnection("www.google.co.uk", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        print("Internet access available.")
        return True
    except Exception:
        conn.close()
        print("ERROR: Internet access not available.")
        return False

check_internet()

def get_Host_name_IP():
    import socket
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Your hostname :  ", host_name)
        print("Your host IP address : ", host_ip)
    except:
        print("Unable to get your hostname and IP, check your connection")

get_Host_name_IP()

def get_location():
    import geocoder
    g = geocoder.ip('me')
    print("Provider co-ordinates : ",g.latlng)

get_location()

def get_provname():

    from bs4 import BeautifulSoup
    import requests
    url= "https://www.whoismyisp.org"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    print(soup.h1.text, ":", soup.p.text)

get_provname()

def get_animation():
    import time
    import sys

    animation = "*."

    for i in range(500):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print
    "End!"

get_animation()
