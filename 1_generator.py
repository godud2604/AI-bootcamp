# %% 일반 함수 => 제너레이터 
def square_numbers(nums):
    result = []

    for i in nums:
        result.append(i * i)

    return result

my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)

"""
- 제너레이터는 자신이 리턴할 모든 값을 메모리에 저장하지 않기 때문에, 조금 전 일반 함수의 결과와 같이 한 번에 리스트로 보이지 않는 것.
- 제너레이터는 한 번 호출될 때마다, 하나의 값만을 전달(yield) 한다.
- 즉 23번줄의 #1까지는 아직 아무런 계산을 하지 않고 누군가가 다음값에 대해서 물어보기를 기다리고 있는 상태
"""
def square_numbers_generator(nums):
    for i in nums:
        yield i * i

my_nums_generator = square_numbers_generator([1, 2, 3, 4, 5]) #1
print(my_nums_generator) # <generator object square_numbers_generator at 0x107e40900>
print(next(my_nums_generator)) # 1
print(next(my_nums_generator)) # 4
print(next(my_nums_generator)) # 9
print(next(my_nums_generator)) # 16
print(next(my_nums_generator)) # 25

"""
StopIteration 예외가 발생하였습니다. 더 이상 전달할 값이 없다는 뜻입니다.
"""
# print(next(my_nums_generator)) 

# %% 제너레이터 - for 루프 통해서 호출
def square_numbers_generator(nums):
    for i in nums:
        yield i * i

my_nums_generator = square_numbers_generator([1, 2, 3, 4, 5])

for num in my_nums_generator:
    print(num)

"""
- 아래의 값이 순차적으로 출력된다.
- 모든 값이 출력되고 StopIteration 예외는 발생하지 않는다. for 루프는 자신이 어디서 멈춰야 하는지 알고 있다.
"""
# 1
# 4
# 9
# 16
# 25

# %% 제너레이터 - list comprehension
# 일반 함수
my_nums = [x*x for x in [1,2,3,4,5]]

print(my_nums) # [1, 4, 9, 16, 25]

for num in my_nums:
    print(num)

# 제너레이터
# #1의 "[]"를 "()"로 바꾸니 제너레이터가 생성됨.
my_nums_generator = (x*x for x in [1, 2, 3, 4, 5])  #1

print(my_nums_generator)

for num in my_nums_generator:
    print(num)
# %% for 루프를 사용하지 않고 한 번에 제너레이터 데이터 보기
my_nums = (x*x for x in [1,2,3,4,5]) # 제너레이터 생성

print(my_nums)
print(list(my_nums)) # 제너레이터를 리스트로 변환

# %% 
import os
import psutil
import random
import time

names = ['최용호', '지길정', '진영욱', '김세훈', '오세훈', '김민우']
majors = ['컴퓨터 공학', '국문학', '영문학', '수학', '정치']

process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss / 1024 / 1024

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

# %%

t1 = time.time()
people = people_list(50)  # 1 people_list를 호출
t2 = time.time()
mem_after = process.memory_info().rss / 1024 / 1024
total_time = t2 - t1

print('시작 전 메모리 사용량: {} MB'.format(mem_before))
print('종료 후 메모리 사용량: {} MB'.format(mem_after))
print('총 소요된 시간: {:.6f} 초'.format(total_time))
# %%
t1 = time.time()
people = people_generator(50)  # 1 people_generator를 호출
t2 = time.time()
mem_after = process.memory_info().rss / 1024 / 1024
total_time = t2 - t1

for num in people:
    print(num)

print('시작 전 메모리 사용량: {} MB'.format(mem_before))
print('종료 후 메모리 사용량: {} MB'.format(mem_after))
print('총 소요된 시간: {:.6f} 초'.format(total_time))
# %%
