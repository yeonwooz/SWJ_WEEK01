# 9663 N-Queen
# 대칭을 제거하지 않음 (Python3 시간초과, PyPy 통과)

import sys

N = int(sys.stdin.readline())

# pos = [0] * N # i열에서 Queen이 존재하는 행 j을 저장 (여기서는 경우의 수를 세는거니까 저장 안해도 됨)
check_row = [False] * N # j행에 Queen이 있는지 확인
check_diagonal_l = [False] * (2*N-1) # ↙ 방향 대각선에 Queen이 있는지 확인
check_diagonal_r = [False] * (2*N-1) # ↘ 방향 대각선에 Queen이 있는지 확인
cnt = 0 # 가능한 방법의 수

def put():
    global cnt
    cnt += 1

# 정답 체스판을 출력하는 함수
# def put2():
#     for j in range(N):
#         for i in range(N):
#             print ('■' if pos[i]==j else '□', end='' )
#         print()
#     print()

def set(i: int):
    for j in range (N//2):
        if (    not check_row[j] 
            and not check_diagonal_l[i+j] 
            and not check_diagonal_r[i-j+N-1]):
            # pos[i] = j
            if i==(N-1):
                put()
            else:
                check_row[j] = check_diagonal_l[i+j] = check_diagonal_r[i-j+N-1] = True
                set(i+1)
                check_row[j] = check_diagonal_l[i+j] = check_diagonal_r[i-j+N-1] = False

set(0)
print(cnt)



