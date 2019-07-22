import unittest
import requests
from app import FabricList
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class NetworkTestCase(unittest.TestCase):
# Sample run 2 2
    def testNetwork(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        fabric = FabricList()
        x = fabric.login()
        data = json.loads(fabric.getNetwork(x))
        for check in data:
            assert check["networkStatus"] == "DEPLOYED"



if __name__ == '__main__':
    unittest.main()
