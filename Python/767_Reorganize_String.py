"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

using heapy to implement max heap
"""
import heapq as hq

class Solution:
    def reorganizeString(self, s: str) -> str:
        dic, res = {}, []
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        max_count = max(v for v in dic.values())
        if max_count > (len(s) + 1) / 2:
            return ''            
        lst = [(-v, k) for k,v in dic.items()]
        hq.heapify(lst)        
        pre = None
        while lst:
            cnt, cur = hq.heappop(lst)
            if pre == cur:
                if not lst:
                    return ''
                else:
                    cnt2, cur2 = hq.heappop(lst)
                    res.append(cur2)
                    pre = cur2
                    hq.heappush(lst, (cnt, cur))
                    if cnt2 < -1:
                        hq.heappush(lst, (cnt2 + 1, cur2))
            else:
                res.append(cur)
                pre = cur
                if cnt < -1:
                        hq.heappush(lst, (cnt + 1, cur))
        return ''.join(res)
