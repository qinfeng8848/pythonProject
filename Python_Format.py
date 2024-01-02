department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456
# 字符串格式化表达式-传统技术
line1="Department1 name:%-10s Manager:%-10s COURSE_FEES:%-10.2f  The End!" % (department1,depart1_m,COURSE_FEES_SEC)
# 字符串格式化方法
tmp = "Department1 name:{0:<10} Manager:{1:<10} COURSE_FEES:{2:<10.2f}  The End!"
line2=tmp.format(pdepartment2,depart2_m,COURSE_FEES_Python)
length = len(line1)
print('='*length)
print(line1)
print (line2)
print('='*length)