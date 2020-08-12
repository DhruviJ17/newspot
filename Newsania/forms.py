from django.forms import ModelForm
from .models import News

class NewsData(ModelForm):
    class Meta:
        model = News
        fields = '__all__'