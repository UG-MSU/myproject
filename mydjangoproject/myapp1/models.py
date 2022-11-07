from datetime import date

from django.db import models


class contest(models.Model):
    id_contest = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=255)
    Contest = models.Manager()

    def __str__(self):
        return self.name


class task(models.Model):
    id_task = models.BigAutoField(primary_key=True)
    statement = models.CharField(blank=True, max_length=255)
    Task = models.Manager()


class user(models.Model):
    id_user = models.BigAutoField(primary_key=True)
    password = models.CharField(blank=True, max_length=255)
    name = models.CharField(blank=True, max_length=255)
    role = models.IntegerField(blank=True)
    User = models.Manager()

    def __str__(self):
        return self.name


class test(models.Model):
    id_test = models.BigAutoField(primary_key=True)
    id_task = models.ForeignKey('task', on_delete=models.CASCADE, blank=True)
    timelimit = models.IntegerField(blank=True)
    input = models.CharField(blank=True, max_length=255)
    output = models.CharField(blank=True, max_length=255)
    Test = models.Manager()


class submission(models.Model):
    id_sub = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey('user', on_delete=models.CASCADE, blank=True)
    id_task = models.ForeignKey('task', on_delete=models.CASCADE, blank=True)
    id_contest = models.ForeignKey('contest', on_delete=models.CASCADE, blank=True)
    timestamp = models.DateField()
    status = models.CharField(blank=True, max_length=255)
    executable_path = models.CharField(blank=True, max_length=255)
    lang = models.CharField(blank=True, max_length=255)
    Submission = models.Manager()


class report_sub(models.Model):
    id_report_sub = models.BigAutoField(primary_key=True)
    id_sub = models.ForeignKey('submission', on_delete=models.CASCADE, blank=True)
    type = models.IntegerField(blank=True)
    text_sub = models.CharField(blank=True, max_length=255)
    pend_rew = models.CharField(blank=True, max_length=255)
    Report_sub = models.Manager()


class review_message(models.Model):
    id_review_message = models.BigAutoField(primary_key=True)
    id_report_sub = models.ForeignKey('report_sub', on_delete=models.CASCADE, blank=True)
    rew = models.CharField(blank=True, max_length=255)
    Review_message = models.Manager()


class legend(models.Model):
    id_legend = models.BigAutoField(primary_key=True)
    id_task = models.ForeignKey('task', on_delete=models.CASCADE, blank=True)
    id_contest = models.ForeignKey('contest', on_delete=models.CASCADE, blank=True)
    text = models.CharField(blank=True, max_length=255)
    Legend = models.Manager()


class contest_user(models.Model):
    id_contest_user = models.BigAutoField(primary_key=True)
    id_contest = models.ForeignKey('contest', on_delete=models.CASCADE, blank=True)
    id_user = models.ForeignKey('user', on_delete=models.CASCADE, blank=True)
    Contest_user = models.Manager()


class contest_task(models.Model):
    id_contest_task = models.BigAutoField(primary_key=True)
    id_task = models.ForeignKey('task', on_delete=models.CASCADE, blank=True)
    id_contest = models.ForeignKey('contest', on_delete=models.CASCADE, blank=True)
    Contest_task = models.Manager()


class checker(models.Model):
    id_checker = models.BigAutoField(primary_key=True)
    prog_path = models.CharField(blank=True, max_length=255)
    id_task = models.ForeignKey('task', on_delete=models.CASCADE, blank=True)
    Checker = models.Manager()
