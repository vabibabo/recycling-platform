import wtforms
from wtforms.validators import length, EqualTo
from models import UserModel


class SignupForms(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=10)])
    password = wtforms.StringField(validators=[length(min=6)])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    def validate_username(self, filed):
        username = filed.data
        user_model = UserModel.query.filter_by(username=username).first()
        if user_model:
            raise wtforms.ValidationError("username has been used! ")


