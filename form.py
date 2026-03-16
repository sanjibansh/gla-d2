from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import PasswordField, StringField, SubmitField
=======
from wtforms import PasswordField,  StringField, SubmitField
>>>>>>> effe0f83e9ccf5f7bfb4b76d1f83f3536c3dc4c6
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
<<<<<<< HEAD
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=25)]
    )
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("New Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(
        "Repeat Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match"),
        ],
    )
    submit = SubmitField("Register")
=======
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
   
>>>>>>> effe0f83e9ccf5f7bfb4b76d1f83f3536c3dc4c6
