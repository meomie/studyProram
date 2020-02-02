def dateRange(year):
	import time
	fmt="%Y-%m-%d"
	bgn=int(time.mktime(time.strptime(year+"-01-01",fmt)))
	end=int(time.mktime(time.strptime(year+"-12-31",fmt)))
	list_date=[time.strftime(fmt,time.localtime(i)) for i in range(bgn,end+1,3600*24)]
	return [i.replace("-","") for i in list_date]
def areIdOk(id1,yl,id2):
	from id_validator import validator
	#validator.is_valid()
	for i in yl:
		if validator.is_valid(id1+i+id2):
			print(id1+i+id2)
areIdOk(input(),dateRange(input()),input())
