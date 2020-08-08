#BOJ-1157
def coundting_word(w) :
    alpabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    checking=list() #알파벳별로 카운팅한 숫자를 저장하는 리스트
    R_word=word.lower() #단어를 모두 소문자로 변환해서 R_word에 넣기
    for check in alpabet :
        checking.append(R_word.count(check))
        max_count_alpa=max(checking) #가장 많이 사용된 알파벳의 횟수를 추출
        alpa_dic={key:value for key, value in zip(alpabet,checking)} #alpabet리스트와 checking리스트를 합쳐서 alpa_dic이라는 딕셔너리 생성
    if checking.count(max_count_alpa)>=2 : #만약 가장 많이 사용된 알파벳의 횟수가 2번 이상이면
        print("?")
    else :
        for key, value in alpa_dic.items() : #딕셔너리에서 value로 key찾기
            if value==max_count_alpa :
                print(key.upper())
word=input()
coundting_word(word)



    