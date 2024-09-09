from django.contrib.auth.models import User
from rest_framework import serializers


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'nickname', 'birthday',
                  'gender', 'intro')

        extra_kwargs = {
            'gender': {'required': False},
            'bio': {'required': False}
        }

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("유저네임 중복")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("이메일 중복")
        return value

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            nickname=validated_data['nickname'],
            birthday=validated_data['birthday'],
            gender=validated_data.get('gender', ''),
            bio=validated_data.get('bio', '')
        )
        user.set_password(validated_data['password'])  # 비밀번호 해시 처리
        user.save()
        return user
