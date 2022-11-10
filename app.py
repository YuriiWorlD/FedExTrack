from flask import Flask, request, render_template

from main.track.api import FedExTrackingApi
from main.track.model import TrackForm
from flask_bootstrap import Bootstrap

from utils.common import parse_response

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='901bab172b32dfdc1dbae4c45e241a0b')
Bootstrap(app)

URL = 'https://wsbeta.fedex.com:443/web-services'
AUTH = {
    'parent_key': 'HicUfijJZSUAtqAG',
    'parent_password': '2IX4AJyvWW9WltylOvw3RokcN',
    'user_key': 'mIAfOSJ0e32Zc4oV',
    'user_password': 'gvTG2nBBVKwZq9dWJnBnJ7rVH',
    'client_account': '602091147',
    'client_meter': '118785166',
}


@app.route('/', methods=['GET', 'POST'])
def tracking_info():
    form = TrackForm(request.form)
    if request.method == 'POST' and form.validate():
        track_number = request.form['tracking_number']
        api = FedExTrackingApi(auth=AUTH)

        try:
            resp = api.track(url=URL, track_id=track_number)
        except ConnectionError:
            return 'Carrier server is unavailable at the moment'
        if resp.status_code != 200:
            return 'FedEx API response error'

        json_response = parse_response(resp)
        return render_template('tracking.html', form=form, response=json_response)

    return render_template('tracking.html', form=form)


if __name__ == '__main__':
    app.run()
