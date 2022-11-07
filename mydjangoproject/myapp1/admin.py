from django.contrib import admin

from myapp1.models import contest, task, user, test, submission, report_sub, review_message, legend, contest_user, \
    contest_task, checker

admin.site.register(contest)
admin.site.register(user)
admin.site.register(task)
admin.site.register(test)
admin.site.register(submission)
admin.site.register(report_sub)
admin.site.register(review_message)
admin.site.register(legend)
admin.site.register(contest_user)
admin.site.register(contest_task)
admin.site.register(checker)
