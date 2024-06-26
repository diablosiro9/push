# Generated by Django 3.2.10 on 2024-04-22 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
        ('users', '0003_user_current_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_game_user', to='games.game'),
        ),
        migrations.AlterField(
            model_name='user',
            name='current_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_game_user', to='games.game'),
        ),
    ]
