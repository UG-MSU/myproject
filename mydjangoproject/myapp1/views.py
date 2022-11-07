from django.shortcuts import render

from django.http import HttpResponse

from django.db import connection

from myapp1.models import contest, task, user, test, submission, report_sub, review_message, legend, contest_user, \
    contest_task, checker

from django.db.models import Manager


def index_page(request):
    return render(request, 'index.html')


def about_page(request):
    idv = user.User.get(name="Вася Пупкин")
    cu = contest_user.Contest_user.filter(id_user=idv.id_user)
    return HttpResponse(list(cu)[0].id_contest)

def about_page2(request):
    idv = user.User.get(name="Вася Пупкин")
    cu = submission.Submission.filter(id_user=idv.id_user)
    cu1 = cu.filter(timestamp="2022-10-31")
    a = []
    for el in cu1:
        a.append([el.timestamp, el.id_sub])
    a.sort()
    b = [el[1] for el in a]
    return HttpResponse(b)

def about_page3(request):
    res = task.Task.raw("SELECT * FROM myapp1_task JOIN myapp1_checker ON myapp1_checker.id_task_id = myapp1_task.id_task WHERE myapp1_checker.prog_path LIKE '%exe%'")
    a = []
    for el in res:
        a.append(el.statement)
    return HttpResponse(a)

def about_page4(request):
    res = task.Task.raw("SELECT *, COUNT(*)  FROM myapp1_task JOIN myapp1_submission ON myapp1_submission.id_task_id = myapp1_task.id_task JOIN myapp1_report_sub ON myapp1_report_sub.id_sub_id = myapp1_submission.id_sub WHERE myapp1_report_sub.type = 0 GROUP BY myapp1_task.id_task ORDER BY COUNT(*)")
    a = []
    for el in res:
        a.append(el.statement)
    return HttpResponse(a)