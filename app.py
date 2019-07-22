import requests
import json
import urllib
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class FabricList():

    def __init__(self):
        self.headers = {'Accept': 'application/json',
                        'Content-Type': 'application/json; charset=UTF-8'}
        self.expirationTime = 999999999
        self.url = 'https://172.25.74.49'
        self.auth = HTTPBasicAuth('admin', 'Cisco12345!')
        #self.fabric = input("Enter name for Fabric: ")
        #self.vrf = input("Enter name for VRF: ")
        #self.network = input("Enter name for Network: ")
        self.fabric = "F"
        self.vrf = "V"
        self.network = "N"

    def login(self):
        payload = {'expirationTime': self.expirationTime}
        postURL = self.url + '/rest/logon'
        response = requests.post(postURL, auth=self.auth,
                             headers=self.headers, data=json.dumps(payload), verify=False)
        dcnm_token = json.loads(response.text)['Dcnm-Token']
        self.headers = (json.loads(response.text))
        print(dcnm_token)
        return dcnm_token


    def getFabricList(self):
        postURL = self.url + '/rest/control/fabrics'
        response = requests.get(postURL, auth=self.auth,
                                headers=self.headers, verify=False)
        print(response.content)
        return response.text

    def getDCNMVersion(self):
        postURL = self.url + '/rest/dcnm-version'
        response = requests.get(postURL, auth=self.auth,
                                headers=self.headers, verify=False)
        print(response.content)
        return response.text

    # Get name of Fabric to be created
    def textToJSON(self):
        with open("Easy_Fabric_11_1_payload.txt", "rb") as fin:
            json_data = json.load(fin)
            val = self.fabric
            json_data.update(fabricName=val)
        with open('data.txt', 'w') as f:
            json.dump(json_data,f)


    def create_easy_fabric(self,dcnm_token):
        hdr = {'Dcnm-Token': dcnm_token, 'Content-Type':'application/json'}
        easy_fabric_payload_file = "data.txt"
        with open(easy_fabric_payload_file, "r") as fin:
            read_txt = fin.read().replace('False', '\"False\"')
            read_txt = read_txt.replace('\"\"False\"\"', '\"False\"')
            read_txt = read_txt.replace('True', '\"True\"')
            payloadFromFabric = json.loads(read_txt.rstrip())
            postURL = self.url + '/rest/control/fabrics'
            response = requests.post(postURL, auth=self.auth,headers=hdr,
                                 data=json.dumps(payloadFromFabric),verify=False)
        #print(response.content)
        #return response.text






        #print(json_data)

    def import_switches(self, dcnm_token):

        payloadSpine={
        "seedIP": "172.25.74.58",
        "snmpV3AuthProtocol": 0,
        "username": "admin",
        "password": "Cisco123!",
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
            "ipaddr": "172.25.74.58",
            "platform": "N9K-9000v",
            "version": "9.2(3)",
            "lastChange": "",
            "hopCount": 0,
            "deviceIndex": "leaf(9NCHKKHXDBN)",
            "statusReason": ""
        }
            ]
        }


        postURL = self.url + '/rest/control/fabrics/' + self.fabric + '/inventory/discover'
        hdr = {'Dcnm-Token': dcnm_token, 'Content-Type': 'application/json'}
        responseSpine = requests.post(postURL,
                                      data=json.dumps(payloadSpine),
                                      headers=hdr,
                                      verify=False)

    def setLAN_credentials(self,dcnm_token):

        postURL = self.url + '/fm/fmrest/lanConfig/saveDefaultCredentials'


        body = urllib.parse.urlencode({
            "username": "admin",
            "password": "Cisco123!",
            "privProtocol": "N/A"
        })
        headers = {'Dcnm-Token': dcnm_token, 'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(postURL,
                                 data=body,
                                 headers=headers,
                                 verify=False)
        print("Dun")

    def save_fabric(self,dcnm_token):
        hdr = {'Dcnm-Token': dcnm_token, 'Content-Type': 'application/json'}
        postURL = self.url + '/rest/control/fabrics/' + self.fabric + '/config-save'
        responseConfig = requests.post(postURL,
                                       headers=hdr,
                                       verify=False)
        print("Sav")
    def deploy_fabric(self, dcnm_token):
        hdr = {'Dcnm-Token': dcnm_token, 'Content-Type': 'application/json'}
        forceShowRun=False
        postURL = self.url + '/rest/control/fabrics/' + self.fabric + '/config-deploy'
        responseConfig = requests.post(postURL,
                                      headers=hdr,
                                      verify=False)
        print("DepDon")


    #CICD if fabricname is same then and only then push
    def createVRF(self,dcnm_token):

        postURL = self.url + '/rest/top-down/fabrics/' + self.fabric + '/vrfs'
        payload = {
            "fabric": self.fabric,
            "vrfName": self.vrf,
            "vrfTemplate": "Default_VRF_Universal",
            "vrfExtensionTemplate": "Default_VRF_Extension_Universal",
            "vrfTemplateConfig": "{\"advertiseDefaultRouteFlag\":\"true\",\"vrfVlanId\":\"\",\"isRPExternal\":\"false\",\"vrfDescription\":\"\",\"L3VniMcastGroup\":\"239.1.1.0\",\"maxBgpPaths\":\"1\",\"maxIbgpPaths\":\"2\",\"vrfSegmentId\":\"50000\",\"ipv6LinkLocalFlag\":\"true\",\"mtu\":\"9216\",\"multicastGroup\":\"\",\"vrfRouteMap\":\"FABRIC-RMAP-REDIST-SUBNET\",\"configureStaticDefaultRouteFlag\":\"true\",\"advertiseHostRouteFlag\":\"false\",\"vrfVlanName\":\"\",\"trmEnabled\":\"false\",\"loopbackNumber\":\"\",\"tag\":\"12345\",\"rpAddress\":\"\",\"nveId\":\"1\",\"asn\":\"65000\",\"vrfIntfDescription\":\"\",\"vrfName\":\"V\"}",
            "vrfId": 50000
            }

        hdr = {'Dcnm-Token': dcnm_token, 'Content-Type': 'application/json'}
        response = requests.post(postURL,
                    data=json.dumps(payload),
                    headers=hdr,
                    verify=False)
        print("C")



    def createNetwork(self,dcnm_token):
        postURL = self.url + '/rest/top-down/fabrics/' + self.fabric + '/networks'
        payload={
            "fabric": self.fabric,
            "networkName": self.network,
            "networkId": 1,
            "networkTemplate": "Default_Network_Universal",
            "networkExtensionTemplate": "Default_Network_Extension_Universal",
            "networkTemplateConfig": "{\"suppressArp\":\"false\",\"secondaryGW2\":\"\",\"secondaryGW1\":\"\",\"loopbackId\":\"\",\"vlanId\":\"100\",\"gatewayIpAddress\":\"\",\"enableL3OnBorder\":\"false\",\"networkName\":\"N\",\"vlanName\":\"\",\"enableIR\":\"false\",\"mtu\":\"\",\"rtBothAuto\":\"false\",\"isLayer2Only\":\"false\",\"intfDescription\":\"\",\"segmentId\":\"1\",\"mcastGroup\":\"239.1.1.0\",\"gatewayIpV6Address\":\"\",\"dhcpServerAddr2\":\"\",\"trmEnabled\":\"false\",\"dhcpServerAddr1\":\"\",\"tag\":\"12345\",\"nveId\":\"1\",\"vrfDhcp\":\"\",\"vrfName\":\"V\"}",
            "vrf": self.vrf
        }
        hdr = {'Dcnm-Token': dcnm_token, 'Content-Type': 'application/json'}
        response = requests.post(postURL,
                                 data=json.dumps(payload),
                                 headers=hdr,
                                 verify=False)


    def attach_network(self, dcnm_token):

        postURL = self.url + '/rest/top-down/fabrics/' + self.fabric + '/networks/attachments'

        payload= [
            {
            "networkName": self.network,
            "lanAttachList": [
            {
            "fabric": self.fabric,
            "networkName": self.network,
            "serialNumber": "9NCHKKHXDBN",
            "switchPorts": "",
            "detachSwitchPorts": "",
            "vlan": 100,
            "dot1QVlan": 1,
            "untagged": False,
            "deployment": True,
            "extensionValues": "",
            "instanceValues": "",
            "freeformConfig": ""
            }
            ]
            }
            ]




        headers = {'Dcnm-Token': dcnm_token, 'Content-Type': 'application/json'}
        response = requests.post(postURL,
                                 data=json.dumps(payload),
                                 headers=headers,
                                 verify=False)

        print(response.content)
        return response.text

    def deployNetwork(self, dcnm_token):


        postURL = self.url + '/rest/top-down/fabrics/' + self.fabric + '/networks/deployments'

        payload={
            "networkNames": self.network
        }
        headers = {'Dcnm-Token': dcnm_token, 'Content-Type': 'application/json'}
        response = requests.post(postURL,
                                 data = json.dumps(payload),
                                 headers=headers,
                                 verify=False)
        print(response.content)

    def getNetwork(self,dcnm_token):
        postURL = self.url + '/rest/top-down/fabrics/' + self.fabric + '/networks'
        headers = {'Dcnm-Token': dcnm_token, 'Content-Type': 'application/json'}
        response = requests.get(postURL, auth=self.auth,
                                headers=headers, verify=False)
        print(response.content)
        return (response.text)

if __name__ == "__main__":
    fabricL = FabricList()
    x = fabricL.login()
    fabricL.getFabricList()
    fabricL.getDCNMVersion()
    fabricL.textToJSON()
    fabricL.create_easy_fabric(x)
    fabricL.import_switches(x)
    fabricL.setLAN_credentials(x)
    fabricL.save_fabric(x)
    fabricL.deploy_fabric(x)
    fabricL.createVRF(x)
    fabricL.createNetwork(x)
    fabricL.attach_network(x)
    fabricL.deployNetwork(x)
    fabricL.getNetwork(x)



