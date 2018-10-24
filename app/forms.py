from wtforms import Form, StringField, IntegerField, DateField
from wtforms.validators import DataRequired, AnyOf


class LatestBusinessDayForm(Form):
    country = StringField('country', validators=[DataRequired(), AnyOf(['UK', 'NL'])])
    current_date = DateField('current_date', default=None)
    shifted_days = IntegerField('shifted_days', default=None)
