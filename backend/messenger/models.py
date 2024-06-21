from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Message(models.Model):
    message_types = [
        ('ORGL', 'original'),
        ('RPLY', 'reply'),
        ('FWRD', 'forwarded'),
    ]
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField(max_length=1000)
    message_type = models.CharField(max_length=4, choices=message_types, default=message_types[0][1])
    original_message = models.ForeignKey('self', on_delete=models.CASCADE, related_name='type_of_message', null=True, blank=True)
    is_sent = models.BooleanField()
    is_seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Message #{self.id}'