import re

"匹配1开头的手机号码"
phone_number = "17727274116"
pattern = re.compile(r"^study_day\d{10}$")
result = re.findall(pattern, phone_number)
print(result)



"匹配邮箱地址"
email = "myemail@gmail.com"
pattern = re.compile(r"^\w+@\w+\.\w+$")
result = re.findall(pattern, email)
print(result)

