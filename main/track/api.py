import requests


class FedExTrackingApi:

    def __init__(self, auth):
        self.parent_key = auth['parent_key']
        self.parent_password = auth['parent_password']
        self.user_key = auth['user_key']
        self.user_password = auth['user_password']
        self.client_account = auth['client_account']
        self.client_meter = auth['client_meter']

    def track(self, url, track_id):
        with open('utils/files/track_request.xml', 'r') as payload_file:
            payload_xml = payload_file.read()

        payload = payload_xml.format(parent_key=self.parent_key,
                                     parent_password=self.parent_password,
                                     user_key=self.user_key,
                                     user_password=self.user_password,
                                     client_account=self.client_account,
                                     client_meter=self.client_meter,
                                     tracking_number=track_id)
        headers = {
            'Content-Type': 'text/xml',
        }

        response = requests.request('POST', url, headers=headers, data=payload)
        return response
