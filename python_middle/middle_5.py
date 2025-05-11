def func(n):
    if n>= 19:
        return True
    else:
        return False
ages=[30,45,20,18,38]
print("결과값:")
#for a in filter(func,ages):
    #print(a)
for a in filter(lambda x:x>=19,ages):
    print(a)
"""
    람다함수
    = 익명의 함수
    = 간단한 기능 수행, 빠르게 작성
    = 다른 함수의 매개변수를 전달할때 사용
    = 복잡한 로직 / 여러줄 코드가 있는 경우에는 함수를 사용하는것이 좋다 => 재사용이 안된다
"""
# lambda 매개변수:표현식 (구현)
"""
    def 함수(매개변수)
        구현
"""
def add(x,y):
    return x+y
val=add(10,20)
print(val)
"""
    let add=(x,y)=>{return x+y}
    add(10,20)
    
    map / reduce
    ---   ------
    count / 단어
    ------------ 하둡 (word count)
                 몽고디비 / ElasticSearch
                 -------  --------------
                 | NoSql = CRUD
"""
add=lambda x,y:x+y
print(type(add))
print(add(10,50))

print((lambda x:x+1)(5))

sum = lambda a,b:a*b
print(sum(10,20))