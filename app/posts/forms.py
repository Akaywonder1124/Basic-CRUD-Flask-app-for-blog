from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired
class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    post_img = FileField("Add featured Image", validators=[FileAllowed(["jpg", "png", "jpeg"],
                                 message="File format not supported")])
    categories = SelectField("Choose Categories", choices=[('Uncategorized', 'Uncategorized'),
                                                    ('Amebo', 'Amebo'), 
                                                    ('Education', 'Education'),  
                                                    ('Sports', 'Sports'), 
                                                    ('Fashion', 'Fashion'), 
                                                    ('Politics', 'Politics'), 
                                                    ('Music', 'Music'),],
                             validators=[DataRequired()])                       
    submit = SubmitField("Post")

class UpdatePostForm(FlaskForm):
    title = StringField("Title")
    content = TextAreaField("Content")
    post_img = FileField("Add featured Image", validators=[FileAllowed(["jpg", "png", "jpeg"],
                                 message="File format not supported")])
    categories = SelectField("Choose Categories", choices=[('Uncategorized', 'Uncategorized'),
                                                    ('Amebo', 'Amebo'), 
                                                    ('Education', 'Education'),  
                                                    ('Sports', 'Sports'), 
                                                    ('Fashion', 'Fashion'), 
                                                    ('Politics', 'Politics'), 
                                                    ('Music', 'Music'),],
                             validators=[DataRequired()])                       
    submit = SubmitField("Update")
