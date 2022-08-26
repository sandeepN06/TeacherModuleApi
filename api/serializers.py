from rest_framework import serializers
from .models import UserModel
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["user_id","cumulative_score"]
        