import requests
import webbrowser

# Syntax Cookie
RbxSecurity = ""

def GenerateAuthTicket():
    r = requests.post('https://www.syntax.eco/Login/NewAuthTicket', cookies={".ROBLOSECURITY": RbxSecurity})
    if r.status_code == 200:
        return r.text
    else:
        print(f"Failed to get Auth Ticket. Error: {r.text}")

def LaunchClient(placeId, year):
    authTicket = GenerateAuthTicket()
    authticket2 = GenerateAuthTicket()

    webbrowser.open(f"syntax-player://1+launchmode:play+gameinfo:{authTicket}+placelauncherurl:https://www.syntax.eco/Game/placelauncher.ashx?placeId={placeId}&t={authticket2}+k:l+clientyear:{year}")
    
LaunchClient(2574, "2016") # Place Id | Year (2016 - 2018)
