from django.shortcuts import render_to_response
from django.http import HttpResponse
from check_in_app.models import CONFERENCE
from django.db import connection
from _datetime import datetime
# Create your views here.
def index(req):
    return render_to_response('index.html')

def condition_add(condition, str1):
    if condition:
        if condition.find(str1) == -1: 
            str1 = " and " + str1 
            condition += str1
    else:
        condition = ' where '+str1
    return condition

def check_in(req):
    errors = []
    persons=[]
    btn_name=""
    try:
        if 'btn_name' in req.GET:
            btn_name=req.GET['btn_name']
        if 'btn_search'in req.GET:
            cursor = connection.cursor()
            sql = "select * from conference"
            condition=''
            print(req.GET)
            if 'name' in req.GET:
                name=req.GET['name']
                if len(name)>0:
                    query="name='"+name+"'"
                    condition=condition_add(condition, query)
            if 'company' in req.GET:
                company =req.GET['company']
            if 'sex' in req.GET:
                sex =req.GET['sex']
            if 'cardid' in req.GET:
                cardid =req.GET['cardid']
            sql = sql+condition+";"
            print(sql)
            cursor.execute(sql)
            desc = cursor.description
            rows = [ dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            sum1 = len(rows)
            for row in rows:
                nametemp = row['name']
                print(nametemp)
                person = CONFERENCE.objects.get(name=nametemp)
                print(person.pay)
                persons.append(person)
                print(persons)
            return render_to_response('check_in.html',{'persons':persons})
#         if 'btn_add' or 'add' in req.GET:
        if btn_name == "add":
            print(req.GET)
            print(req.POST)
            conference=CONFERENCE()
            conference.name=req.GET['name']
            conference.sex=req.GET['sex']
            print('性别')
            print(conference.sex)
            conference.cardid=req.GET['cardid']
            conference.company=req.GET['company']
            conference.department=req.GET['department']
            conference.degree=req.GET['degree']
            conference.title=req.GET['title']
            conference.post=req.GET['post']
            conference.phone=req.GET['phone']
            conference.registtime=datetime.now()
#             conference.pay=string.atoi(req.GET['pay'])
            conference.banknum=req.GET['banknum']
            conference.bankname=req.GET['bankname']
            conference.room=req.GET['room']
#             conference.hoteldays=string.atoi(req.GET['hoteldays'])
            conference.ticketnum=req.GET['ticketnum']
            conference.score=req.GET['score']
            conference.save()
            print(conference)
            print(req.GET)
            return render_to_response('check_in.html', {'errors': errors})
        if 'btn_edit' in req.GET:
            print(req.GET)
        if 'btn_delete' in req.GET:
            print(req.GET)
    except Exception as err:
        errors.append(err)
        print(err)  
        return render_to_response('check_in.html', {'errors': errors})
    return render_to_response('check_in.html')
