from rest_framework import serializers

from .models import FAQ

class FAQTopicSerialzer(serializers.Serializer):
    topic=serializers.CharField(read_only=True)
    id=serializers.IntegerField(read_only=True)
    
class FaqSerlizer(serializers.ModelSerializer):
    url=serializers.HyperlinkedIdentityField(view_name='faq_detail',lookup_field='slug')
    topic=FAQTopicSerialzer(many=True)
    class Meta:
        model=FAQ
        fields=['url','title','content','topic','date_posted']
