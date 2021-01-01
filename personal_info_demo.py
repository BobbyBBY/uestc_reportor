#  这里修改为你自己的信息，注释下的都需要修改

from datetime import datetime
NEED_DATE = datetime.now().strftime("%Y-%m-%d")
# 报平安信息
daily_report_data = {
    # 学号
    "USER_ID": "2020xxxx",
    # 姓名
    "USER_NAME": "xxx",
    # 学院
    "DEPT_NAME": "计算机科学与工程学院（网络空间安全学院）",
    # 性别
    "GENDER_CODE": "男",
    # 年龄
    "AGE": "21",
    # 电话
    "PHONE_NUMBER": "XXXXXX",
    # 身份证
    "IDCARD_NO": "xxxxxx",
    # 全日制学术硕士 || 电子信息
    "LB": "全日制学术硕士",
    # 学院代码
    "DEPT_CODE": "1008",
    # 导师
    "TUTOR": "xxxx",
    "WID": "B63D65084785EE87E053D3A4C5DEA774",
    "NEED_CHECKIN_DATE": NEED_DATE,
    "CZR": "",
    "CZZXM": "",
    "CZRQ": NEED_DATE+" 00:00:00",
    "PERSON_TYPE_DISPLAY": "留校",
    "PERSON_TYPE": "001",
    "LOCATION_PROVINCE_CODE_DISPLAY": "四川省",
    "LOCATION_PROVINCE_CODE": "510000",
    "LOCATION_CITY_CODE_DISPLAY": "成都市",
    "LOCATION_CITY_CODE": "510100",
    "LOCATION_COUNTY_CODE_DISPLAY": "郫都区",
    "LOCATION_COUNTY_CODE": "510117",
    # 校区 
    "LOCATION_DETAIL": "电子科技大学清水河校区",
    "HEALTH_STATUS_CODE_DISPLAY": "正常",
    "HEALTH_STATUS_CODE": "001",
    "HEALTH_UNSUAL_CODE": "",
    "IS_HOT_DISPLAY": "否",
    "IS_HOT": "0",
    "IS_IN_HB_DISPLAY": "否",
    "IS_IN_HB": "0",
    "IS_HB_BACK_DISPLAY": "否",
    "IS_HB_BACK": "0",
    "IS_DEFINITE_DISPLAY": "否",
    "IS_DEFINITE": "0",
    "IS_QUARANTINE_DISPLAY": "否",
    "IS_QUARANTINE": "0",
    "IS_KEEP_DISPLAY": "否",
    "IS_KEEP": "0",
    "TEMPERATURE": "",
    "IS_SEE_DOCTOR_DISPLAY": "否",
    "IS_SEE_DOCTOR": "NO",
    "IS_IN_SCHOOL_DISPLAY": "是",
    "IS_IN_SCHOOL": "1",
    "MEMBER_HEALTH_STATUS_CODE_DISPLAY": "正常",
    "MEMBER_HEALTH_STATUS_CODE": "001",
    "MEMBER_HEALTH_UNSUAL_CODE_DISPLAY": "",
    "MEMBER_HEALTH_UNSUAL_CODE": "",
    "REMARK": "",
    "SAW_DOCTOR_DESC": "",
}
# 体温信息
temp_report_data = {}
temp_report_data['USER_ID'] = daily_report_data['USER_ID']
temp_report_data['USER_NAME'] = daily_report_data['USER_NAME']
temp_report_data['DEPT_NAME'] = daily_report_data['DEPT_NAME']
temp_report_data['DEPT_CODE'] = daily_report_data['DEPT_CODE']


login_data = {
    # 学号
    "username":'',
    # 密码
    "password":'',
}