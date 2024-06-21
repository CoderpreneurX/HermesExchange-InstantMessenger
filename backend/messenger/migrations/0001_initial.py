# Generated by Django 5.0.6 on 2024-06-21 09:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000)),
                ('message_type', models.CharField(choices=[('ORGL', 'original'), ('RPLY', 'reply'), ('FWRD', 'forwarded')], default='original', max_length=4)),
                ('is_sent', models.BooleanField()),
                ('is_seen', models.BooleanField(default=False)),
                ('original_message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type_of_message', to='messenger.message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
