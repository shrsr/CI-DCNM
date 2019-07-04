import requests
import json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class FabricList():

    def __init__(self):
        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json; charset=UTF-8'}
        self.expirationTime = 999999

    def login(self):
        payload = {'expirationTime': self.expirationTime}
        response = requests.post('https://10.60.0.191/rest/logon', auth=HTTPBasicAuth('admin', 'Cisco12345'),
                             headers=self.headers, data=json.dumps(payload), verify=False)
        dcnm_token = json.loads(response.text)['Dcnm-Token']
        self.headers = (json.loads(response.text))
        print(dcnm_token)
        return dcnm_token


    def getFabricList(self):
        response = requests.get('https://10.60.0.191/rest/control/fabrics', auth=HTTPBasicAuth('admin', 'Cisco12345'),
                                headers=self.headers, verify=False)
        print(response.content)

    def getDCNMVersion(self):
        response = requests.get('https://10.60.0.191/rest/dcnm-version', auth=HTTPBasicAuth('admin', 'Cisco12345'),
                                headers=self.headers, verify=False)
        print(response.content)
        return response.text

    def create_easy_fabric(self,dcnm_token):
        hdr = {'Dcnm-Token': dcnm_token, 'Content-Type':'application/json'}
        easy_fabric_payload_file = "Easy_Fabric_11_1_payload.txt"
        with open(easy_fabric_payload_file, "r") as fin:
            read_txt = fin.read().replace('False', '\"False\"')
            read_txt = read_txt.replace('\"\"False\"\"', '\"False\"')
            read_txt = read_txt.replace('True', '\"True\"')
            payloadFromFabric = json.loads(read_txt.rstrip())
            response = requests.post('https://10.60.0.191/rest/control/fabrics', auth=HTTPBasicAuth('admin', 'Cisco12345'),headers=hdr,
                                 data=json.dumps(payloadFromFabric),verify=False)
        #print(response.content)
        #return response.text

    def import_switches(self, dcnm_token):

        payloadSpine={
        "seedIP": "10.60.0.103",
        "snmpV3AuthProtocol": 0,
        "username": "admin",
        "password": "Cisco12345",
        "maxHops": 2,
        "cdpSecondTimeout": 0,
        "preserveConfig": False,
        "switches": [
        {
            "reachable": True,
            "auth": True,
            "known": True,
            "valid": True,
            "selectable": True,
            "sysName": "spine",
            "ipaddr": "10.60.0.103",
            "platform": "N9K-C9236C",
            "version": "9.2(3)",
            "lastChange": "string",
            "hopCount": 0,
            "deviceIndex": "spine(FDO20060E3B)",
            "statusReason": "string"
        }
            ]
        }

        hdr = {'Dcnm-Token': dcnm_token, 'Content-Type': 'application/json'}
        responseSpine = requests.post('https://10.60.0.191/rest/control/fabrics/CICD/inventory/discover',
                                      data=json.dumps(payloadSpine),
                                      headers=hdr,
                                      verify=False)



        payloadLeaf1 = {
              "seedIP": "10.60.0.155",
              "snmpV3AuthProtocol": 0,
              "username": "admin",
              "password": "Cisco12345",
              "maxHops": 2,
              "cdpSecondTimeout": 0,
              "preserveConfig": False,
              "switches": [
                {
                  "reachable": True,
                  "auth": True,
                  "known": True,
                  "valid": True,
                  "selectable": True,
                  "sysName": "leaf",
                  "ipaddr": "10.60.0.155",
                  "platform": "N9K-C9372PX-E",
                  "version": "9.2(3)",
                  "lastChange": "string",
                  "hopCount": 0,
                  "deviceIndex": "leaf(FDO204323ZJ)",
                  "statusReason": "string"
                }
              ]
            }




        responseLeaf1 = requests.post('https://10.60.0.191/rest/control/fabrics/CICD/inventory/discover',
                                 data=json.dumps(payloadLeaf1),
                                 headers=hdr,
                                 verify=False)

        payloadLeaf2= {
            "seedIP": "10.60.0.41",
            "snmpV3AuthProtocol": 0,
            "username": "admin",
            "password": "Cisco12345",
            "maxHops": 2,
            "cdpSecondTimeout": 0,
            "preserveConfig": False,
            "switches": [
                {
                    "reachable": True,
                    "auth": True,
                    "known": True,
                    "valid": True,
                    "selectable": True,
                    "sysName": "leaf",
                    "ipaddr": "10.60.0.41",
                    "platform": "N9K-C92160YC-X",
                    "version": "9.2(3)",
                    "lastChange": "string",
                    "hopCount": 0,
                    "deviceIndex": "leaf(SAL2009ZMSX)",
                    "statusReason": "string"
                }
            ]
        }

        responseLeaf2 = requests.post('https://10.60.0.191/rest/control/fabrics/CICD/inventory/discover',
                                      data=json.dumps(payloadLeaf2),
                                      headers=hdr,
                                      verify=False)




if __name__ == "__main__":
    fabricL = FabricList()
    fabricL.login()
    fabricL.getFabricList()
    fabricL.getDCNMVersion()
    fabricL.create_easy_fabric(fabricL.login())
    fabricL.import_switches(fabricL.login())

