# 기존 딕셔너리
my_dict = {"old_key": "value1", "another_key": "value2"}

# 키를 변경하고 싶은 경우
old_key = "old_key"  # 변경하려는 기존 키
new_key = "new_key"  # 새로운 키

# 새로운 키를 추가하고 기존 키의 값을 가져와서 할당한 후 기존 키 삭제
my_dict[new_key] = my_dict.pop(old_key)

# 딕셔너리 내용 확인
print(my_dict)