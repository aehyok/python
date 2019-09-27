#create by 矜持的折返跑
import time
import requests
import pymysql
config={
    "host":"111.231.215.64",
    "user":"sa",
    "password":"M9y2512!",
    "database":"aehyok",
    "charset":"utf8"
}
def lagou(page,position):
    headers = {'Referer':'https://www.lagou.com/jobs/list_'+position+'?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',              
                'Origin':'https://www.lagou.com',                
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
                'Accept':'application/json, text/javascript, */*; q=0.01'
               }
    dates={'first':'true',
           'pn': page,
           'kd': position}
    url='https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'
    urls='https://www.lagou.com/jobs/list_python'

    #每次调用获取cookies-防止调用失败
    cook=requests.Session()
    cook.get(url=urls,headers=headers,timeout=3)
    resp = requests.post(url,data=dates,headers=headers,cookies=cook.cookies)
    print(resp.text)
    result=resp.json()['content']['positionResult']['result']

    #写入mysql数据库
    db = pymysql.connect(**config)
    positionName = []
    for i in result:
        print(i)
        count=0
        positionName.append(i['positionName'])
        timeNow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #连接数据库
        cursor = db.cursor()
        if i['businessZones']:
            businessZones = "".join(i['businessZones'])
        else:
            businessZones=""

        if i['companyLabelList']:
            companyLabelList = "".join(i['companyLabelList'])
        else:
            companyLabelList=""

        if i['industryLables']:
            industryLables = "".join(i['industryLables'])
        else:
            industryLables=""

        if i['positionLables']:
            positionLables = "".join(i['positionLables'])
        else:
            positionLables=""

        sql = "insert into lagou(positionName,workYear,salary,companyShortName\
              ,companyIdInLagou,education,jobNature,positionIdInLagou,createTimeInLagou\
              ,city,industryField,positionAdvantage,companySize,score,positionLables\
              ,industryLables,publisherId,financeStage,companyLabelList,district,businessZones\
              ,companyFullName,firstType,secondType,isSchoolJob,subwayline\
              ,stationname,linestaion,resumeProcessRate,createByMe,keyByMe\
        )VALUES (%s,%s,%s,%s, \
              %s,%s,%s,%s,%s\
              ,%s,%s,%s,%s,%s,%s,%s\
              ,%s,%s,%s,%s,%s\
              ,%s,%s,%s,%s,%s\
              ,%s,%s,%s,%s,%s\
              )"
        cursor.execute(sql,(i['positionName'],i['workYear'],i['salary'],i['companyShortName']
                            ,i['companyId'],i['education'],i['jobNature'],i['positionId'],i['createTime']
                            ,i['city'],i['industryField'],i['positionAdvantage'],i['companySize'],i['score'],positionLables
                            ,industryLables,i['publisherId'],i['financeStage'],companyLabelList,i['district'],businessZones
                            ,i['companyFullName'],i['firstType'],i['secondType'],i['isSchoolJob'],i['subwayline']
                            ,i['stationname'],i['linestaion'],i['resumeProcessRate'],timeNow,position
                            ))
        db.commit()  #提交数据
        cursor.close()
        count=count+1
    db.close()
def main(position):
            page = 1
            while page<=30:
                print('---------------------第',page,'页--------------------')
                lagou(page,position)
                page=page+1
#输入你想要爬取的职位名,如:python
if __name__ == '__main__':
    main('python')
