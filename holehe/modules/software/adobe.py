from holehe.core import *
from holehe.localuseragent import *

def adobe(email):
    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-IMS-CLIENTID': 'adobedotcom2',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://auth.services.adobe.com',
        'DNT': '1',
        'Connection': 'keep-alive',
    }

    data = '{"username":"' + email + '","accountType":"individual"}'
    r = requests.post(
        'https://auth.services.adobe.com/signin/v1/authenticationstate',
        headers=headers,
        data=data).json()
    if "errorCode" in str(r.keys()):
        return({"rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
    headers['X-IMS-Authentication-State'] = r['id']
    params = (
        ('purpose', 'passwordRecovery'),
    )
    response = requests.get(
        'https://auth.services.adobe.com/signin/v2/challenges',
        headers=headers,
        params=params).json()
    return({"rateLimit": False, "exists": True, "emailrecovery": response['secondaryEmail'], "phoneNumber": response['securityPhoneNumber'], "others": None})
