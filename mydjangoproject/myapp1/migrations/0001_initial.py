# Generated by Django 4.1.2 on 2022-10-31 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contest',
            fields=[
                ('id_contest', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='report_sub',
            fields=[
                ('id_report_sub', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField(blank=True)),
                ('text_sub', models.CharField(blank=True, max_length=255)),
                ('pend_rew', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='task',
            fields=[
                ('id_task', models.BigAutoField(primary_key=True, serialize=False)),
                ('statement', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id_user', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('role', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id_test', models.BigAutoField(primary_key=True, serialize=False)),
                ('timelimit', models.IntegerField(blank=True)),
                ('input', models.CharField(blank=True, max_length=255)),
                ('output', models.CharField(blank=True, max_length=255)),
                ('id_task', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.task')),
            ],
        ),
        migrations.CreateModel(
            name='submission',
            fields=[
                ('id_sub', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateField()),
                ('status', models.CharField(blank=True, max_length=255)),
                ('executable_path', models.CharField(blank=True, max_length=255)),
                ('lang', models.CharField(blank=True, max_length=255)),
                ('id_contest', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.contest')),
                ('id_task', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.task')),
                ('id_user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.user')),
            ],
        ),
        migrations.CreateModel(
            name='review_message',
            fields=[
                ('id_review_message', models.BigAutoField(primary_key=True, serialize=False)),
                ('rew', models.CharField(blank=True, max_length=255)),
                ('id_report_sub', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.report_sub')),
            ],
        ),
        migrations.AddField(
            model_name='report_sub',
            name='id_sub',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.submission'),
        ),
        migrations.CreateModel(
            name='legend',
            fields=[
                ('id_legend', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(blank=True, max_length=255)),
                ('id_contest', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.contest')),
                ('id_task', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.task')),
            ],
        ),
        migrations.CreateModel(
            name='contest_user',
            fields=[
                ('id_contest_user', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_contest', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.contest')),
                ('id_user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.user')),
            ],
        ),
        migrations.CreateModel(
            name='contest_task',
            fields=[
                ('id_contest_task', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_contest', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.contest')),
                ('id_task', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.task')),
            ],
        ),
        migrations.CreateModel(
            name='checker',
            fields=[
                ('id_checker', models.BigAutoField(primary_key=True, serialize=False)),
                ('prog_path', models.CharField(blank=True, max_length=255)),
                ('id_task', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp1.task')),
            ],
        ),
    ]
