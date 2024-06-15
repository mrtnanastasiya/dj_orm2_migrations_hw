from django.db import migrations, models

def copy_field(apps, schema):
    Student = apps.get_model('school', 'Student')
    for student in Student.objects.all():
        student.teachers.add(student.teacher)

class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_add_teachers'),
    ]

    operations = [

        migrations.RunPython(code=copy_field),

    ]
