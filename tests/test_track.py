import json
import unittest
from unittest.mock import MagicMock

from utils.common import parse_response


expected_response = {
    "carrier": "FedEx\n                    Express",
    "carrier_code": "FDXE",
    "tracking_number": "794887075005",
    "tracking_number_id": "XXXXXXXXXX~XXXXXXXXXXXX~FX",
    "status": "Shipment information sent to\n                        FedEx",
    "checkpoints": [
        {
            "description": "Shipment information sent to\n                        FedEx",
            "location": {
                "city": None,
                "state_code": None,
                "country_code": None,
                "country": None,
                "residential": "false"
            },
            "time": "2016-11-17T03:13:01-06:00"
        }
    ]
}


class TestTracking(unittest.TestCase):

    def test_tracking_info_success(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        with open('utils/files/track_response.xml', 'r') as response_file:
            resp = response_file.read()
        mock_response.text = resp

        self.assertEqual(parse_response(mock_response),
                         json.dumps(expected_response, indent=4, separators=(',', ': ')))
