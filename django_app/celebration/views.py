# celebration/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Relay, Blessing
from .serializers import BlessingSerializer

@api_view(['POST'])
def relay(request):
    """
    接力接口：每调用一次就新增一条 Relay 记录，
    并返回当前的接力总次数。
    """
    Relay.objects.create()
    total = Relay.objects.count()
    return Response({'visitorNum': total})

@api_view(['GET'])
def relay_count(request):
    """
    获取当前接力总次数，不新增记录。
    """
    total = Relay.objects.count()
    return Response({'visitorNum': total})


@api_view(['POST'])
def bless_send(request):
    """
    发送祝福接口：接收 {"content": "..."}，
    新建一条 Blessing（默认 is_approved=False），
    并返回创建的记录（只含 id 和 content）。
    """
    content = request.data.get('content', '').strip()
    if not content:
        return Response(
            {'detail': '祝福内容不能为空'},
            status=status.HTTP_400_BAD_REQUEST
        )

    blessing = Blessing.objects.create(content=content)
    return Response(
        {'id': blessing.id, 'content': blessing.content},
        status=status.HTTP_201_CREATED
    )


@api_view(['GET'])
def bless_list(request):
    """
    获取祝福列表接口：只返回已通过审核的祝福 content 列表。
    """
    qs = Blessing.objects.all().order_by('-created_at')
    # qs = Blessing.objects.filter(is_approved=True).order_by('-created_at')
    contents = list(qs.values_list('content', flat=True))
    return Response(contents)
