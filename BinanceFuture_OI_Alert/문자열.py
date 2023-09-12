import unicodedata

def calculate_width(input_string):
    total_width = 0

    for char in input_string:
        width = unicodedata.east_asian_width(char)
        if width in ('W', 'F'):
            total_width += 2  # 전체 너비 문자
        else:
            total_width += 1  # 반각 너비 문자

    return total_width

print(calculate_width('DODOX'))
print(calculate_width('1000XEC'))
# print(unicodedata.east_asian_width(''))

# def pad_to_width(input_string, desired_width):
#     current_width = calculate_width(input_string)
#     if current_width >= desired_width:
#         return input_string  # 이미 원하는 너비 이상이면 그대로 반환

#     # 공백의 갯수를 너비 차이에 맞게 조절
#     num_spaces = desired_width - current_width

#     # 반각 문자를 전체 너비로 채우기 위해 공백을 절반으로 나눠 사용
#     half_width_spaces = ' ' * (num_spaces // 2)

#     # 전체 너비와 반각 너비를 더하여 원하는 너비를 만듦
#     formatted_string = input_string + half_width_spaces * 2

#     return formatted_string

# # OI 상위 10개 메세지 전송
# Descend_OI_Message = ''
# for i in range(10):
#     Descend_OI_Message += (str(Descend_OI[i])+'\n')

# # 줄바꿈 문자('\n')를 기준으로 메세지를 분리하고, 각 행을 가공
# lines = Descend_OI_Message.strip().split('\n')
# formatted_message = ''

# # 코인 이름과 값의 최대 길이 찾기
# max_coin_length = max(len(pair.split('/')[0]) for pair in lines)
# max_value_length = max(len(str(eval(line)[1])) for line in lines)

# for line in lines:
#     pair, value = eval(line)  # 문자열을 튜플로 변환
#     coin, currency = pair.split('/')
#     value_str = '${:,.0f}'.format(value)  # 숫자를 USD 형식으로 포맷팅
#     # coin과 value_str 값을 적절한 길이로 맞춰서 출력
#     formatted_line = f'{coin.split("/")[0]: <{max_coin_length}} : {value_str: >{max_value_length}}\n'
#     formatted_message += formatted_line

# # 원하는 너비
# desired_width = 40

# # 문자열의 너비 계산 후 원하는 너비로 맞추기
# formatted_message = pad_to_width(formatted_message, desired_width)

# OI_Alert_send_message_to_jandi(formatted_message)
