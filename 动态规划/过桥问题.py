# 问题描述
# https://blog.csdn.net/fengyud/article/details/4647139
# 用了堆来做优先队列

from itertools import combinations  # 组合
import heapq


def through_bridge(heapSrc, heapDest, totalTime, seq1=[], seq2=[]):
    if len(heapSrc) == 2:
        first = heapq.heappop(heapSrc)
        second = heapq.heappop(heapSrc)
        # print('A->B', first, second)
        heapq.heappush(heapDest, first)
        heapq.heappush(heapDest, second)
        seq1.append(first)
        seq1.append(second)
        # print('前向')
        # for item in seq1:
        #     print(item)
        # print('反向')
        # for item in seq2:
        #     print(item)
        print(totalTime + max([first, second]))
    elif len(heapSrc) >= 3:
        for i, combination in enumerate(combinations(heapSrc, 2)):
            man1, man2 = combination
            # go
            heapSrc_clone = heapSrc.copy()
            heapDest_clone = heapDest.copy()
            heapSrc_clone.remove(man1)
            heapSrc_clone.remove(man2)
            heapq.heappush(heapDest_clone, man1)
            heapq.heappush(heapDest_clone, man2)

            # back
            # backman = heapq.heappop(heapDest_clone)
            seq1_clone = seq1.copy()
            seq1_clone.append(man1)
            seq1_clone.append(man2)
            seq2_clone = seq2.copy()

            man = heapq.heappop(heapDest_clone)
            heapq.heappush(heapSrc_clone, man)
            seq2_clone.append(man)
            now_time = totalTime + max(combination) + man
            through_bridge(heapSrc_clone, heapDest_clone, now_time, seq1_clone, seq2_clone)


heapA = [1, 2, 5, 10]
heapB = []
heapq.heapify(heapA)
through_bridge(heapA, heapB, 0)
