from __future__ import absolute_import, unicode_literals
from celery import task
from datetime import datetime

from shortener.models import Site, DailyLog


@task()
def clear_click_count():
    for site in Site.objects.all():
        daily_log = DailyLog(site=site, log_date=datetime.today())
        daily_log.save()
        site.click_count = 0
        site.save()


