from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='autonomo_foco',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='round',
            name='autonomo_pontuacao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='round',
            name='teleoperado_foco',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='round',
            name='teleoperado_pontuacao',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
