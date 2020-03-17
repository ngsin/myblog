from django.shortcuts import render
from blog2 import models
from django.utils import timezone
import markdown
# Create your views here.


def index(request):

    singles = models.ExampleModel.objects.all()
    return render(request, 'blog2/index.html', {'singles': singles, })


def single_page(request, single_id):


    data = {}  # data用于向模板传递数据
    single = models.ExampleModel.objects.get(pk=single_id) # 获取正被打开的博客
    data['single'] = single

    next_blog = models.ExampleModel.objects.filter(id__gt=single.id).order_by('id')
    pre_blog = models.ExampleModel.objects.filter(id__lt=single.id).order_by('-id')

    # 取第1条记录
    if pre_blog.count() > 0:
        pre_blog = pre_blog[0]
    else:
        pre_blog = None

    if next_blog.count() > 0:
        next_blog = next_blog[0]
    else:
        next_blog = None


    single.content = markdown.markdown(single.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    data['pre_blog'] = pre_blog
    data['next_blog'] = next_blog

    return render(request, 'blog2/single.html', data, )


def pre_page(request):
    # previous blog（上一篇）
    sql = "select id from blog2_examplemodel where id>%s order by id limit 1" % (id)
    single_ids = models.ExampleModel.objects.raw(sql)
    if len(list(single_ids)) > 0:
        single_id = single_ids[0]
    else:
        single_id = None

    single = models.ExampleModel.objects.get(pk=single_id)

    single.content = markdown.markdown(single.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    return render(request, 'blog2/single.html', {'single': single}, )

