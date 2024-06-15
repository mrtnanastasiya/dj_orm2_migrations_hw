from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_copy_teacher_data'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),

    ]
