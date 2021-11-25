import sys
import heapq

def getSkyline(self, buildings):
    # 이벤트 처리
    # 입력 받아서 리스트에 넣기
    # 높이를 -로 넣는 건 이후 최대 힙에 넣을때나 
    # result 리스트의 최근값과 최대 높이를 비교할 때 사용
    events = [[L, -H, R] for L, R, H in buildings]

    # 건물이 끝나는 위치를 추가로 저장
    events += [[R, 0, 0] for _, R, _ in buildings]
    # x좌표를 기준으로 정렬
    events.sort()

    
    # res: result, [x, height]
    # live: heapq, (-height, x)
    # live는 최대 힙. 즉 루트 노드는 힙에 들어있는 가장 높은 건물
    res = [[0,0]]   # 첫 입력값과 비교를 위한 더미 데이터
    live = [(0, float('inf'))]

    for position, negH, R in events:
        # step1. 이미 지나간 건물 시작,끝위치 pop
        # 지금 힙에 있는 최댓값보다 현재 포지션이 작으면 빼기
        while live[0][1] <= position:
            heapq.heappop(live)
            
        # step2. starting event
        # (negH != 0)이면 live에 넣기
        if negH:
            heapq.heappush(live, (negH, R))
        
        # step3. result 리스트의 마지막 값과 높이의 최댓값이 다를 경우 Insert
        if res[-1][1] != -live[0][0]:
            res.append([position, -live[0][0]])
    return res[1:]