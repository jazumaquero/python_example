from urllib.parse import urlencode

from flask import Blueprint, render_template, request, redirect

from calendars.services import latest_business_day
from .forms import *

frontend = Blueprint('frontend', __name__, url_prefix='/frontend')


@frontend.route('/<country>')
def index(country):
    kwargs = request.args.to_dict()
    kwargs['country'] = country
    return render_template('index.html', country=country, latest_business_day=latest_business_day(**kwargs))


@frontend.route('/form', methods=['GET', 'POST'])
def form():
    form = LatestBusinessDayForm(request.form)
    if request.method == 'POST' and form.validate():
        query_parameters = {}
        if form.current_date:
            query_parameters['current_date'] = form.current_date.data
            query_parameters['shifted_days'] = form.shifted_days.data
        url = f'frontend/{form.country.data}?{urlencode(query_parameters)}'
        return redirect(url)
    return render_template('latest_business_day.html', form=form)


@frontend.errorhandler(ValueError)
def bad_request(error):
    return render_template('400.html', error=str(error))
