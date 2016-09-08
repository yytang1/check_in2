# -*- coding: utf-8 -*-
import xlwt
from check_in_app.models import CONFERENCE
def exportData(filename):
	datas = CONFERENCE.objects.all()
	file = xlwt.Workbook(encoding = 'utf-8')
	table = file.add_sheet('sheet 1')
	row = 0
	col = 0
	
	head_list = [u'姓名',u'性别',u'身份证号',u'工作单位',u'科室',u'学历',u'职称',u'职务',u'联系电话',u'签到时间',u'注册费',u'银行卡号',u'开户行',u'房间号',u'住宿天数',u'奖券号',u'学分号']
	for head in head_list:
		table.write(row,col,head)
		col += 1
	row += 1
	for data in datas:
		_id = data.id
		name = data.name
		if data.sex == 0:
			sex = '男'
		else:
			sex = '女'
		cardid = data.cardid
		company = data.company
		department = data.department
		degree = data.degree
		title = data.title
		post = data.post
		phone = data.phone
		registtime = data.registtime
		pay = data.pay
		banknum = data.banknum
		bankname = data.bankname
		room = data.room
		hoteldays = data.hoteldays
		ticketnum = data.ticketnum
		score = data.score

		res = [name,sex,cardid,company,department,degree,title,post,phone,registtime,pay,banknum,bankname,room,hoteldays,ticketnum,score]

		for index in range(len(res)):
			if res[index] == None:
				res[index] = ' '
			table.write(row,index,res[index])
		

		row += 1
	file.save(u'D:\\%s.xls' % filename)
	return [u'导出成功']