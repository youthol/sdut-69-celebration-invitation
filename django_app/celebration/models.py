# celebration/models.py

from django.db import models

class Relay(models.Model):
    """
    每一次“接力”动作都会创建一条记录，
    统计接力总次数可通过 Relay.objects.count() 实现。
    """
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '接力记录'
        verbose_name_plural = '接力记录'

    def __str__(self):
        return f"Relay @ {self.created_at:%Y-%m-%d %H:%M:%S}"


class Blessing(models.Model):
    """
    存储用户提交的留言／祝福内容，以及审核状态和审核人。
    """
    content = models.TextField('祝福内容')
    created_at = models.DateTimeField('提交时间', auto_now_add=True)

    # —— 新增审核字段 —— 
    is_approved = models.BooleanField(
        '是否审核通过',
        default=False,
        help_text='True 表示已通过审核，False 表示待审核或未通过'
    )
    approved_by = models.IntegerField(
        '审核人 ID',
        null=True,
        blank=True,
        help_text='审核人用户表中的主键 ID，未审核时留空'
    )
    approved_at = models.DateTimeField(
        '审核时间',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = '祝福留言'
        verbose_name_plural = '祝福留言'

    def __str__(self):
        snippet = (self.content[:20] + '…') if len(self.content) > 20 else self.content
        status = '✅' if self.is_approved else '⏳'
        return f"{status} {snippet} ({self.created_at:%m-%d %H:%M})"
