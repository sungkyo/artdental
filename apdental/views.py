from django.db.models.functions import Trim
from django.shortcuts import render, redirect
from .models import ImgInfo, SogeView, TbReservation, TbPatientInfo, TbReservation, TbResveInfo
from django.db.models import Q, Subquery
import csv, time, datetime

subquery_sql = ImgInfo.objects.values('chart').order_by('-C_Date').annotate(trimmed_chart=Trim('chart')).values('trimmed_chart')[:1]
context = {}
current =  datetime.datetime.now()
tmp_dt = datetime.datetime.strptime('2023/07/26 11:00:00', "%Y/%m/%d %H:%M:%S")

BeforTime = -1

def resve_list(request):
    print("<----- resve_list: ")
    StartTime = current
    ReSult = TbResveInfo.objects.filter(begin_datetime__gt=tmp_dt).order_by('begin_datetime')

    for ReSults in ReSult:
        if (ReSults.dlay_mi > 0):
            BeforTime = ReSults.dlay_mi
            StartTime = ReSults.begin_datetime
        #print(f'start_time:{StartTime + datetime.timedelta(minutes=15)}')
        # if (ReSults.begin_datetime > StartTime + datetime.timedelta(minutes=15)):
        #     ReSults.dlay_time = ReSults.begin_datetime + datetime.timedelta(minutes=BeforTime)
        #     ReSults.dlay_mi = BeforTime + ReSults.dlay_mi
        #     print(f'BeforTime:{(BeforTime)} - begin_datetime:{(ReSults.begin_datetime )} - dlay_time:{(ReSults.dlay_time)}')
    context['ReSult'] = ReSult
    return render(request, "apdental/resve_list.html", context)

def imp_patient_info(request):
    print("<=imp_patient_info: ")
    CSV_PATH_PRODUCTS = 'static/file/vw_RESERVATION.csv'
    patient_data = []
    with open(CSV_PATH_PRODUCTS) as csv_file:
        rows = csv.reader(csv_file, delimiter = ',')
        data_reader = csv.reader(csv_file)
        #next(data_reader, None)
        for row in rows:
            rsData = TbResveInfo.objects.create(
                pnt_id=row[0].strip(),
                begin_datetime = datetime.datetime.strptime(row[1].strip(), "%Y%m%d%H%M%S"),
                font_color = row[2].strip(),
                back_color = row[3].strip(),
                pnt_name = row[4].strip(),
                resi_no = row[5].strip(),
                expc_tm = 0,
                dlay_mi = 0)
            rsData.save()
    return redirect('resve_list') # 화면에 data가 보이지 않을 때

def clnic_epct_list(request):
    print(f"<----- clnic_epct_list:{current}")
    StartTime = current
    ReSult = TbResveInfo.objects.filter(begin_datetime__gt=tmp_dt).order_by('begin_datetime')[:8]
    for ReSults in ReSult:
        if (ReSults.dlay_mi > 0):
            BeforTime = ReSults.dlay_mi
            StartTime = ReSults.begin_datetime
        #print(f'start_time:{StartTime + datetime.timedelta(minutes=15)}')
        if (ReSults.begin_datetime > StartTime + datetime.timedelta(minutes=15)):
            ReSults.dlay_mi = BeforTime
    context['ReSult'] = ReSult
    return render(request, "apdental/clnic_epct_list.html", context)
def end_update(request):
    print(f"<----- arvl_time: {request.GET['id']}")
    id = request.GET['id']
    tbresveinfo = TbResveInfo.objects.get(id=id)
    tbresveinfo.end_tm = current
    tbresveinfo.save()
    return render(request, "apdental/resve_list.html", context)

def arvl_update(request):
    print(f"<----- arvl_time: {request.GET['id']}")
    id = request.GET['id']
    tbresveinfo = TbResveInfo.objects.get(id=id)
    tbresveinfo.arvl_tm = current
    tbresveinfo.save()
    return render(request, "apdental/resve_list.html", context)


def dlay_update(request):
    print(f"<----- dlay_update: {request.GET['dlay_mi']}")
    id = request.GET['id']

    tbresveinfo = TbResveInfo.objects.get(id=id)
    if request.POST.get('dlay_mi') != "":
        tbresveinfo.dlay_mi = request.GET['dlay_mi']
        #tbresveinfo.arvl_tm = current
    tbresveinfo.save()
    return redirect('resve_list')


def dental_list(request):

    ReSult =SogeView.objects.filter(chart__in=Subquery(subquery_sql)).values('chart', 'jumin', 'Name')
    #a1 = str(ReSult.values('chart')) # 객체 & value 보기
    a1 = subquery_sql[0]['trimmed_chart'] # value 보기
    print("<=dental_list: "+a1 )

    context['ReSult'] = ReSult
    return render(request, "apdental/dental_list.html", context)

def dental_chart_search(request):
    searchKey = request.POST.get("search")
    print("<=dental_chart_search: "+searchKey)
    ReSult =SogeView.objects.filter(Name=searchKey).values('chart', 'jumin', 'Name')

    context['ReSult'] = ReSult
    context['search'] = searchKey
    return render(request, "apdental/dental_list.html", context)

def dental_date_search(request):
    if request.GET.get('c_search', ''):
        c_searchKey = request.GET.get('c_search', '')
        searchKey = request.GET.get('search', '')
    else:
        searchKey = subquery_sql[0]['trimmed_chart']
        c_searchKey = subquery_sql[0]['trimmed_chart']
    #searchKey = request.GET['search']
    print("<=dental_date_search:" + str(searchKey))
    #os.system("xcopy 1.txt 2.* /C/Y/i/D:" + str(datetime.today().strftime('%m-%d-%Y') ))

    ReSult = SogeView.objects.filter(Q(Name=searchKey) | Q(chart=searchKey)).values('chart', 'jumin', 'Name')
    ReImgInfo = (ImgInfo.objects.extra(select={'CT_ype':"(CASE WHEN C_Type = 1 THEN 'p' WHEN C_Type = 4 THEN 'c' WHEN C_Type = 5 THEN 'k' WHEN C_Type = 2 THEN 's' ELSE 'z' END)"}
                , where=["trim(chart) = '"+c_searchKey+"'"])
        .values('C_Date', 'C_Type', 'seq', 'CT_ype')).order_by('-C_Date')[:4]
    ReToDayImgInfo = (ImgInfo.objects.extra(select={'CT_ype':"(CASE WHEN C_Type = 1 THEN 'p' WHEN C_Type = 4 THEN 'c' WHEN C_Type = 5 THEN 'k' WHEN C_Type = 2 THEN 's' ELSE 'z' END)"}
                , where=["trim(chart) = '"+c_searchKey+"'"])
        .values('C_Date', 'C_Type', 'seq', 'CT_ype')).order_by('-C_Date')[:1]
    context['ReImgInfo'] = ReImgInfo
    context['search'] = searchKey
    context['ReSult'] = ReSult
    context['ReToDayImgInfo'] = ReToDayImgInfo

    return render(request, "apdental/dental_list.html", context)

def dental_photo(request):

    #ReSult = (ImgInfo.objects.extra(select={'Name':"trim(SogeView.Name)", 'jumin':"trim(SogeView.jumin)"} , tables=['SogeView'], where=["trim(imginfo.chart) = trim(SogeView.chart)", "trim(SogeView.Name)= '정원식'"])
    ReSult = (ImgInfo.objects.select_related('sogeview').filter(chart__contains='958')  # join(select_related)
              .values('chart', 'C_Date', 'sogeview__jumin', 'sogeview__Name')) # 따라 SQL 달라짐
    #ReSult = (SogeView.objects.all().prefetch_related("imginfo"))   # join(prefetch_related)

    context['ReSult'] = ReSult
    return render(request, "apdental/dental_photo.html", context)


def jquery_test(request):
    print("<=jquery_test: ")
    return render(request, "apdental/jquerytest.html")


