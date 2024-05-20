from django.db import models

class dbtest(models.Model):
    print('models_dbtest_init')
    id = models.IntegerField(primary_key=True)
    name = models.CharField('名稱', max_length=255)
    add = models.CharField('地址', max_length=255)
    print('name', name)
    #machineGroup = models.CharField(max_length=100)
    #machineItem = models.CharField(max_length=100)
    #field1 = models.CharField(max_length=100)
    #print('field1', field1)
    #field2 = models.IntegerField()
	#machineName = models.CharField(max_length = 255, verbose_name = 'machineName')

    def __str__(self) -> str:
        return self.name


class personnelinformation(models.Model):
    print('models_PersonnelInformation_init')
    id = models.IntegerField('id', primary_key=True)
    joinYear = models.CharField('年分', max_length=255)
    latestLicense = models.CharField('身分', max_length=255)
    identity = models.CharField('等級', max_length=255)
    chineseName = models.CharField('名字', max_length=255)
    mobilePhone = models.CharField('電話', max_length=255)
    idNumber = models.CharField('身分證字號', max_length=255)
    mid = models.CharField('mid', max_length=255)
 
