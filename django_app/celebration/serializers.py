# celebration/serializers.py

from rest_framework import serializers
from .models import Relay, Blessing

class RelaySerializer(serializers.ModelSerializer):
    """
    序列化 Relay 模型，用于统计接力列表或单条详情。
    """
    class Meta:
        model = Relay
        fields = [
            'id',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
        ]


class BlessingSerializer(serializers.ModelSerializer):
    """
    序列化 Blessing 模型，用于前端提交和后台审核展示。
    """
    class Meta:
        model = Blessing
        fields = [
            'id',
            'content',
            'created_at',
            'is_approved',
            'approved_by',
            'approved_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            # 审核相关字段通常由后台填写
            'is_approved',
            'approved_by',
            'approved_at',
        ]
