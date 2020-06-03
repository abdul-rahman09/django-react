from .models import Lawyer
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer2(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('password', 'username', 'email',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer2(User, many=False)
    class Meta:
        model = Lawyer
        # fields  = "__all__"
        fields = ('city', 'state', 'phone_number', 'hcr_number', 'year_admitted',
        'liscence_number', 'user')

    def create(self, validated_data):
        city_data = validated_data.pop('city')
        state_data = validated_data.pop('state')
        phone_number_data = validated_data.pop('phone_number')
        liscence_number_data = validated_data.pop('liscence_number')
        year_admitted_data = validated_data.pop('year_admitted')
        hcr_number_data = validated_data.pop('hcr_number')
        profile_data = validated_data.pop('user')

        user = User.objects.create(**profile_data)
        user.save()
        obj  = Lawyer(user=user,state=state_data,city=city_data,phone_number=phone_number_data,liscence_number=liscence_number_data,year_admitted=year_admitted_data,hcr_number=hcr_number_data)
        obj.save()
        return obj