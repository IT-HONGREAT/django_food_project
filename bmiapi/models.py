from django.db import models
from django.utils import timezone

# Create your models here.


class Predictions(models.Model):
    # The possible predictions the model can make in the 'predictions' field
    # defined by: (<database name>, <human readible name>)
    PREDICT_OPTIONS = [
        ('깡마름', '깡마름'),
        ('마름', '마름'),
        ('보통', '보통'),
        ('통통', '통통'),
        ('뚱뚱', '뚱뚱'),
    ]

    gender_choice = [
        (0,0), #여자
        (1,1), #남자
    ]

    # Prediction table fields (or columns) are defined by creating attributes
    # and assigning them to field instances such as models.CharField()
    
    height = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)
    sex = models.IntegerField(choices=gender_choice)
    prediction = models.CharField(choices=PREDICT_OPTIONS, max_length=10)