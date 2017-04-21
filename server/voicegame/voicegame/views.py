import datetime
import urllib
from django.http import Http404
from django.http import JsonResponse
from voicegame import models


def record(request):
    name = request.GET.get('name')
    score = request.GET.get('score')
    tag = request.GET.get('tag', '')
    ip = request.META.get('REMOTE_ADDR', '0.0.0.0')
    if name and score:
        try:
            models.Log.objects.create(
                name=urllib.unquote(name),
                score=int(score),
                tag=tag,
                ip=ip
            )
        except:
            raise Http404
    return JsonResponse({})


def top(request):
    qs_all = models.Log.objects.order_by('-score')[:10]
    data_all = []
    for q in qs_all:
        d = {}
        d['name'] = q.name
        d['score'] = q.score
        data_all.append(d)
    today = datetime.date.today()
    print today
    qs_today = models.Log.objects.filter(
        create_time__gte=today).order_by('-score')[:10]
    data_today = []
    for q in qs_today:
        d = {}
        d['name'] = q.name
        d['score'] = q.score
        data_today.append(d)
    try:
        score = int(request.GET.get('score', 0))
    except:
        score = 0
    if score:
        all_count = min(models.Log.objects.count() - 1, 1)
        low_count = models.Log.objects.filter(score__lt=score).count()
        rank = '%.2f' % (low_count * 100.0 / all_count)
    else:
        rank = '0.00'
    return JsonResponse({
        'all': data_all,
        'today': data_today,
        'rank': rank
    })
