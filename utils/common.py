import json

from bs4 import BeautifulSoup


def parse_response(resp):
    response_bs = BeautifulSoup(resp.text, 'xml')

    response_dict = {}
    carrier = get_bs_element(response_bs, 'OperatingCompanyOrCarrierDescription')
    response_dict['carrier'] = carrier
    carrier_code = get_bs_element(response_bs, 'CarrierCode')
    response_dict['carrier_code'] = carrier_code
    tracking_number = get_bs_element(response_bs, 'TrackingNumber')
    response_dict['tracking_number'] = tracking_number
    tracking_number_id = get_bs_element(response_bs, 'TrackingNumberUniqueIdentifier')
    response_dict['tracking_number_id'] = tracking_number_id
    status = get_bs_element(response_bs, 'EventDescription')
    response_dict['status'] = status

    checkpoints_list = []
    for response_event in response_bs.find_all('Events'):
        checkpoint = {'description': get_bs_element(response_event, 'EventDescription')}

        location = {'city': get_bs_element(response_event, 'City'),
                    'state_code': get_bs_element(response_event, 'StateOrProvinceCode'),
                    'country_code': get_bs_element(response_event, 'CountryCode'),
                    'country': get_bs_element(response_event, 'CountryName'),
                    'residential': get_bs_element(response_event, 'Residential')}

        checkpoint['location'] = location
        checkpoints_list.append(checkpoint)

        time = get_bs_element(response_event, 'Timestamp')
        checkpoint['time'] = time

    response_dict['checkpoints'] = checkpoints_list
    return json.dumps(response_dict, indent=4, separators=(',', ': '))


def get_bs_element(el, tag):
    return el.find(tag).text if el.find(tag) else None
