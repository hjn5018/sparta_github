# =============================================================================================
for j, k in enumerate(range(10), 1): # 테스트 케이스 10개 받기 // 몇 번인지 enumerate하기
    pal_len = int(input()) # palindrome_length
    for i in range(8): # 한 줄씩받는 input 8번 수행하기
        pane_line = input()
# for i, j in enumerate(range(8), 1): # 인덱스가 필요할 때 enumerate 활용해보기
#     pane_line = input()

# 회문 찾는 코드 작성해보기 -> 글자 크기 4인 str을 먼저 지정해줘야함.
    if str_ == str_[::-1]:
        print("찾았다!")

# 테스트 케이스의 번호를 출력해야하는데, 회문이 없는 테스트 케이스가 있을 수 있다.
# skip할 때는??

# 테스트 케이스의 번호를 출력하는 코드를 작성해보자. -> 위에서 for enumerate했음 // for문 안에 들어가야 계속 출력
    print('#j', '회문의 개수') 

# =====================대강 짜기도 힘드네..........===============================================
# 개선해야할 점
# 입력을 다 받고나서 탐색을 해야하는데, 그러려면 각 글자판에 번호를 매겨주어야한다.
# -> 최상단의 enumerate(j)로 해결이 되는지 확인해야함.

# 각 글자판에 대해 탐색을 해야하는데, 가로뿐만이 아닌 세로도 탐색해야함.
# str_은 가로인데.. 세로의 str_2를 따로 정의해줘야함...

# 글자크기 4인 str을 지정하는 방법은??
# len()??????????????????
# ===========================================
일단 입력 하나만 받아서 해보자...