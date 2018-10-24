from flask import Blueprint, request, jsonify

from calendars.services import latest_business_day

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/latest_business_day/<country>')
def previous_business_days(country):
    kwargs = request.args.to_dict()
    kwargs['country'] = country
    return latest_business_day(**kwargs)


@api.errorhandler(ValueError)
def bad_request(error):
    return jsonify({'message': str(error)}), 400
