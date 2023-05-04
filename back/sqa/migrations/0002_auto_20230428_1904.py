# Generated by Django 4.2 on 2023-04-28 03:07

from django.db import migrations

def fill_tables(apps, schema_editor):
    Question = apps.get_model('sqa', 'Question')

    Question.objects.create(
        title='Math is hard to learn?',
        subject='Math',
        answer='Yes'
    )
    Question.objects.create(
        title='Physics is hard to learn?',
        subject='Physics',
        answer='Yes'
    )
    Question.objects.create(
        title='History is hard to learn?',
        subject='History',
        answer='No'
    )
    # Subject = apps.get_model('sqa', 'Subject')
    # Question = apps.get_model('sqa', 'Question')
    # Answer = apps.get_model('sqa', 'Answer')

    # subject1 = Subject.objects.create(
    #     name='Math'
    # )

    # question1 = Question.objects.create(
    #     name='Math is hard to learn?',
    #     subject=subject1
    # )

    # answer1 = Answer.objects.create(
    #     name='Yes',
    #     is_true=True,
    #     question=question1
    # )
    # answer2 = Answer.objects.create(
    #     name='No',
    #     is_true=False,
    #     question=question1
    # )


class Migration(migrations.Migration):

    dependencies = [
        ('sqa', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_tables)
    ]
