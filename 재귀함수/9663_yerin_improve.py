# 9663 N-Queen
# y축 선대칭 고려 (Python3 통과 가능)

import sys

N = int(sys.stdin.readline())

# pos = [0] * N # i열에서 Queen이 존재하는 행 j을 저장 (여기서는 경우의 수를 세는거니까 저장 안해도 됨)
check_row = [False] * N # j행에 Queen이 있는지 확인
check_diagonal_l = [False] * (2*N-1) # ↙ 방향 대각선에 Queen이 있는지 확인
check_diagonal_r = [False] * (2*N-1) # ↘ 방향 대각선에 Queen이 있는지 확인
cnt = 0 # 가능한 방법의 수

#정답 체스판을 출력하는 함수
# def print_position():
#     for j in range(N):
#         for i in range(N):
#             print ('■' if pos[i]==j else '□', end='' )
#         print()
#     print()


def set(i: int):
    global cnt
    for j in range (N if i else N//2): # N//2 if i!=0 else N
        if (    not check_row[j] 
            and not check_diagonal_l[i+j] 
            and not check_diagonal_r[i-j+N-1]):
            # pos[i] = j
            if i==(N-1):
                # print_position()
                cnt += 1
                return
            else:
                check_row[j] = check_diagonal_l[i+j] = check_diagonal_r[i-j+N-1] = True
                set(i+1)
                check_row[j] = check_diagonal_l[i+j] = check_diagonal_r[i-j+N-1] = False

if N%2 :
    # 홀수일 때 : 첫번째 열에 퀸을 절반만 둬보고 그 때의 경우의 수를 2배로 취한다 (정가운데 제외)
    set(0)
    cnt *= 2
    # 첫번째 열의 정가운데에 퀸을 뒀을 때의 경우의 수를 구해서 더한다.
    j = N//2
    check_row[j] = check_diagonal_l[j] = check_diagonal_r[-j] = True
    set(1)
    print(cnt)
else: 
    # 짝수일 때 : 첫번째 열에 퀸을 절반만 둬보고 그 때의 경우의 수를 2배로 취한다 
    set(0)
    print(cnt*2)
