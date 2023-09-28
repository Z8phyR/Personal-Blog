from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Length
from flask_wtf.file import FileAllowed, FileField


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    # You can further improve how tags are inputted and processed.
    tags = StringField('Tags')
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')


class UpdateProfileForm(FlaskForm):
    bio = TextAreaField('Bio', validators=[Length(max=500)])
    profile_picture = FileField('Profile Picture', validators=[
                                FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')


class SearchForm(FlaskForm):
    query = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')
