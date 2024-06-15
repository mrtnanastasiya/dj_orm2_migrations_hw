from django.db import migrations, models
from django.db.models import F

def copy_field(apps, schema):
    Student = apps.get_model('school', 'Student')
    for student in Student.objects.all():
        student.teachers.add(student.teacher)

class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [

        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),

        # migrations.RunPython(code=copy_field),

        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),

    ]
