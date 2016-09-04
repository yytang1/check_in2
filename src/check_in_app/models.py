from django.db import models

# Create your models here.
class CONFERENCE(models.Model):
    id = models.AutoField(primary_key=True,db_column='id')
    name=models.CharField(max_length=20, db_column='name')
    sex=models.IntegerField(db_column='sex',default=0)
    cardid=models.CharField(max_length=20, db_column='cardid',null=True)
    company=models.CharField(max_length=50, db_column='company',null=True)
    department=models.CharField(max_length=20, db_column='department',null=True)
    degree=models.CharField(max_length=10, db_column='degree',null=True)
    title=models.CharField(max_length=20, db_column='title',null=True)
    post=models.CharField(max_length=20, db_column='post',null=True,blank=True)
    phone=models.CharField(max_length=11, db_column='phone',null=True,blank=True)
    registtime=models.DateField(blank=True,db_column='registtime',null=True)
    pay=models.IntegerField(db_column='pay', null=True,blank=True)
    banknum=models.CharField(max_length=19, db_column='banknum',null=True,blank=True)
    bankname=models.CharField(max_length=30, db_column='bankname',null=True,blank=True)
    room=models.CharField(max_length=10, db_column='room',null=True,blank=True)
    hoteldays=models.IntegerField(db_column='hoteldays', null=True,blank=True)
    ticketnum=models.CharField(max_length=20, db_column='ticketnum',null=True,blank=True)
    score=models.CharField(max_length=20, db_column='score',null=True,blank=True)
    def __str__(self):
        return str(self.id) + '_'+ str(self.name) 
    class Meta:
        db_table = 'conference'