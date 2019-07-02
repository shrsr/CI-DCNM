import unittest
import requests
from app import FabricList
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class MyTestCase(unittest.TestCase):
# Sample run
    def test_version(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        f = FabricList()
        data = json.loads(f.getDCNMVersion())
        assert data["Dcnm-Version"] == "11(1)"

if __name__ == '__main__':
    unittest.main()
