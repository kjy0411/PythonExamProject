import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
"""
    CVS파일 읽기 / CVS파일 추출
    JSON 파싱 / XML 파싱방법
    파이썬 => 변수 (데이터형 확인 => type)
            list / dict
            연산자 / 제어문 / 함수 / 예외처리
            웹 = spring / spring-boot
                        jpa / my-sql
"""
emp_df=pd.read_csv('c:/pydata/EMP.csv')
print(emp_df)
#create table empcp as select * from where deptno=30
#empcp=emp_df[emp_df['DEPTNO']==30]
#print(empcp)
# emp_df => select ename from emp
print(emp_df['ENAME'])
print(emp_df['JOB'])
# empno,ename,job,sal => deptno=20
data=emp_df[emp_df['DEPTNO']==20][['EMPNO','ENAME','JOB','SAL']].copy()
print(data)
# select empno,ename,job from emp where job='manager'
data=emp_df[emp_df['JOB']=='MANAGER'][['EMPNO','ENAME','JOB']].copy()
#emp_df[['EMPNO','ENAME','JOB']][emp_df['JOB']=='MANAGER'] => 컬럼명과 조건의 순서는 관계 없다
print(data)

names=emp_df[['ENAME']]
print(names)
values=emp_df[['SAL']]
print(values)
#df=pd.DataFrame({"names":names,"sals":values})
#print(df)
#plt.bar(names.values.tolist(),
#        values.values.tolist())

#plt.show()