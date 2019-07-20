

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_time']},
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_id',
            field=models.IntegerField(default=0),
        ),
    ]
