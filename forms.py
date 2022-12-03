from flask_wtf import  FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,DataRequired,email
from product import  User

class LoginForm(FlaskForm):
    def validate_email_address(self, email_adress_to_check):
        email_adress= User.query.filter_by(email_address=email_adress_to_check.data).first()


        email_adress=StringField(label='email',validators=[Length(min=2,max=30),DataRequired()])
        password_hash= PasswordField(label='password', validators=[Length(min=6),DataRequired])
        submit= SubmitField(label='login')
