from rest_framework import serializers
from users.models import User
from .models import Help

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # 필요한 필드만을 지정
        fields = ['nickname']

class HelpSerializer(serializers.ModelSerializer):
    #user의 특정 정보 (닉네임 등)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Help
        fields = ['id', 'user', 'title', 'content', 'location', 'latitude', 'longitude', 'created_at', 'updated_at']


# 도움요청 메인 화면 내 마커를 위한 class
class CustomHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ['id', 'latitude', 'longitude']