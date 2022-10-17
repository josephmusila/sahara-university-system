from rest_framework import serializers
from django.conf import settings
from base.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        
        fields=('regNumber','names','idnumber','email','course','department','gender','avatar')
        depth=2
    # course=serializers.StringRelatedField()
    department=serializers.StringRelatedField()
    names=serializers.SerializerMethodField(method_name='student_name')
    # avatar=serializers.SerializerMethodField(method_name="get_profile_picture_url")

    def get_profile_picture_url(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(settings.MEDIA_URL + obj['avatar'])

    def student_name(self,student:Student):
        return f'{student.firstname} {student.otherme} {student.surname}'