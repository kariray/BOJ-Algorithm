#BOJ-10809
def search_alpa(s) :
    alpabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for search in alpabet :
        print(s.find(search), end=' ') #한줄로 출력 되게
    
string = input()
search_alpa(string)
