import requests
import json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class FabricList():

    def __init__(self):
        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json; charset=UTF-8'}
        self.expiration_time = 100000000000000

    def login(self):
        payload = {'expirationTime': self.expiration_time}
        resp = requests.post('https://10.60.0.191/rest/logon', auth=HTTPBasicAuth('admin', 'Cisco12345'),
                             headers=self.headers, data=json.dumps(payload), verify=False)
        self.headers = (json.loads(resp.text))

    def getFabricList(self):
        response = requests.get('https://10.60.0.191/rest/control/fabrics', auth=HTTPBasicAuth('admin', 'Cisco12345'),
                                headers=self.headers, verify=False)
        print(response.content)

    def getDCNMVersion(self):
        response = requests.get('https://10.60.0.191/rest/dcnm-version', auth=HTTPBasicAuth('admin', 'Cisco12345'),
                                headers=self.headers, verify=False)
        print(response.content)
        return response.text


if __name__ == "__main__":
    fabricL = FabricList()
    fabricL.login()
    fabricL.getFabricList()
    fabricL.getDCNMVersion()

