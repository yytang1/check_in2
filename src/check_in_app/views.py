# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from check_in_app.models import CONFERENCE
from django.db import connection
from datetime import datetime
from check_in_app.exportData import exportData
# Create your views here.
def index(req):
    return render_to_response('index.html')

def condition_add(condition, str1):
    if condition:
        if condition.find(str1) == -1: 
            str1 = " and " + str1 
            condition += str1
    else:
        condition = ' where ' + str1
    return condition

def check_in(req):
    errors = []
    persons = []
    btn_name = ""
    try:
        if 'btn_name' in req.GET:
            btn_name = req.GET['btn_name']
        if 'btn_search'in req.GET:
            cursor = connection.cursor()
            sql = "select * from conference"
            condition = ''
            print(req.GET)
            if 'name' in req.GET:
                name = req.GET['name']
                if len(name) > 0:
                    query = "name='" + name + "'"
                    condition = condition_add(condition, query)
            if 'company' in req.GET:
                company = req.GET['company']
            if 'sex' in req.GET:
                sex = req.GET['sex']
            if 'cardid' in req.GET:
                cardid = req.GET['cardid']
            sql = sql + condition + ";"
            print(sql)
            cursor.execute(sql)
            desc = cursor.description
            rows = [ dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            sum1 = len(rows)
            str1=u'共有'+str(sum1)+u'条记录'
            for row in rows:
                nametemp = row['id']
                person = CONFERENCE.objects.get(id=nametemp)
                if person.sex == 0:
                    person.sex = u"女"
                if person.sex == 1:
                    person.sex = u"男"
                persons.append(person)
                print(persons)
                if len(persons)>=20:
                    str1+=u',下面显示20条'
                    break
            errors.append(str1)
            return render_to_response('check_in2.html', {'persons':persons,'errors': errors})
#         if 'btn_add' or 'add' in req.GET:
        if btn_name == "add":
            conference = CONFERENCE()
            conference.name = req.GET['name']
            person_sex = req.GET['sex']
            if person_sex == u'男':
                conference.sex = 1
            if person_sex == u'女':
                conference.sex = 0
            conference.cardid = req.GET['cardid']
            conference.company = req.GET['company']
            conference.department = req.GET['department']
            conference.degree = req.GET['degree']
            conference.title = req.GET['title']
            conference.post = req.GET['post']
            conference.phone = req.GET['phone']
            conference.registtime = datetime.now()
            if req.GET['pay'].isdigit():
                conference.pay = int(req.GET['pay'])
            conference.banknum = req.GET['banknum']
            conference.bankname = req.GET['bankname']
            conference.room = req.GET['room']
            day1 = req.GET['hoteldays']
            if day1.isdigit():
                conference.hoteldays = int(day1)
            conference.ticketnum = req.GET['ticketnum']
            conference.score = req.GET['score']
            conference.save()
            errors.append(u"新增人员成功")
            return render_to_response('check_in2.html', {'errors': errors})
        if 'btn_edit' in req.GET:
            if 'id' in req.GET:
                person_id = req.GET['id']
                if len(person_id) < 1:
                    errors.append(u"修改人员失败，该人员不存在，请仔细检查")
                    return render_to_response('check_in2.html', {'errors': errors})
                conference = CONFERENCE.objects.get(id=person_id)
                conference.name = req.GET['name']
                person_sex = req.GET['sex']
                if person_sex == u'男':
                    conference.sex = 1
                if person_sex == u'女':
                    conference.sex = 0
                conference.cardid = req.GET['cardid']
                conference.company = req.GET['company']
                conference.department = req.GET['department']
                conference.degree = req.GET['degree']
                conference.title = req.GET['title']
                conference.post = req.GET['post']
                conference.phone = req.GET['phone']
                conference.registtime = datetime.now()
                print(datetime.now())
                if req.GET['pay'].isdigit():
                    conference.pay = int(req.GET['pay'])
                conference.banknum = req.GET['banknum']
                conference.bankname = req.GET['bankname']
                conference.room = req.GET['room']
                day1 = req.GET['hoteldays']
                if day1.isdigit():
                    conference.hoteldays = int(day1)
                conference.ticketnum = req.GET['ticketnum']
                conference.score = req.GET['score']
                conference.save()
                errors.append(u"修改信息成功")
                return render_to_response('check_in2.html', {'errors': errors})
            return render_to_response('check_in2.html', {'errors': errors})
        if 'btn_delete' or 'hidd_del' in req.GET:
            values = req.GET.getlist('personCheck[]')
            for value in values:
                person = CONFERENCE.objects.get(id=value)
                person.delete()
            if values:
                errors.append(u'删除人员成功')
            return render_to_response('check_in2.html', {'errors': errors})
    except Exception as err:
        errors.append(err)
        print(err)  
        return render_to_response('check_in2.html', {'errors': errors})
    return render_to_response('check_in2.html')
def export(req):
    messages = []
    if 'export_q' in req.GET and req.GET['export_q'] == 'export':
        if 'filename' in req.GET:
            filename = req.GET['filename']
            if filename == '':
                filename = 'backup'
        messages = exportData(filename)
    return render_to_response('export.html', {'messages':messages})
