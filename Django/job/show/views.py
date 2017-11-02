from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from show.models import job,Condition
from django.db.models import Q

# Create your views here.
def index(request,pIndex):

    #利用get方式可以获取请求，进入列表页时默认第一页
    page=request.GET.get('page',1)
    #薪资默认显示所有
    salary = request.GET.get('salary','')
    #学历默认显示所有
    edu_bg=request.GET.get('edu_bg','')
    #公布时间默认显示所有
    pub_date=request.GET.get('pub_date','')
    #经历默认显示所有
    experience=request.GET.get('experience','')
    #检索关键字
    keywords=request.POST.get('keywords')
    if keywords:
        pass
    else:
        keywords=request.GET.get('keyword')

    #各个条件
    salary_con_list=Condition.objects.filter(type_id=1)
    edu_bg_list=Condition.objects.filter(type_id=2)
    pub_date_list=Condition.objects.filter(type_id=3)
    experience_list=Condition.objects.filter(type_id=4)

    #默认显示60页
    if salary=='' and edu_bg=='' and pub_date=='' and experience=='' and keywords == '':
        list1 = job.objects.all()[0:1800]
    else:
        condition = {}
        if salary:
            condition['salary__icontains'] = salary
        if edu_bg:
            condition['edu_bg__icontains'] = edu_bg
        if pub_date:
            condition['pub_date__icontains'] = pub_date
        if experience:
            condition['experience__icontains'] = experience
        if keywords:
            condition['pos_desc__icontains'] = keywords
        list1 = job.objects.filter(**condition)
        if len(list1) > 1800:
            list1 = job.objects.filter(**condition)[0:1800]


    #实例化分页对象
    p = Paginator(list1,30)
    # 处理当前页号信息
    if pIndex == "":
        pIndex = '1'
    # 获取当前页数据
    if page=="":
        page=1
    else:
        page = int(page)
    list2 = p.page(page)
    plist = p.page_range
    return render(request,
                  'index.html',
                  {'jobslist':list2,
                    'page':page,
                    'lastpage':p.num_pages,
                    'salary_con_list':salary_con_list,
                    'edu_bg_list':edu_bg_list,
                    'pub_date_list':pub_date_list,
                    'experience_list':experience_list,
                    'keywords':keywords,
                    })