#BOJ-5622
alpha_input=input() #알파벳 대문자 입력받기
alpha_list=[] #알파벳을 한글자씩 끊어서 저장할 리스트
dial_num=[] #알파벳에 상응하는 숫자를 저장할 리스트
dial_sum=0 #dial_num리스트에 있는 숫자를 모두 더한 값을 저장
element=0 #dial_num리스트에 있는 요소의 갯수를 저장

#다이얼의 딕셔너리
dial={'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,
    'O': 6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9}

for i in range(0,len(alpha_input)) : #입력받은 알파벳을 한글자씩 끊어서 alpha_list에 저장
    alpha_list.append(alpha_input[i:i+1])

for i in range(0,len(alpha_list)) : #alpha_list에 있는 알파벳을 dial 딕셔너리를 참고하여 숫자로 변환
    dial_num.append(dial.get(alpha_list[i]))

for i in dial_num : #dial_num에 있는 숫자를 모두 더하고, dial_num에 있는 요소의 갯수를 구함
    dial_sum+=i
    element+=1

total_sum=dial_sum+element #dial_num에 있는 숫자를 모두 더한 값과 dial_num에 있는 요소 갯수의 합
print(total_sum) #결과 출력