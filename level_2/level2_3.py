# -*- coding: utf-8 -*-
"""level2_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wp9EgJAiuMbGVYgErzSYBsdI9VZuTbnS
"""

answers = [1,2,3,2,3]

from collections import deque
def solution(prices):
    answer = []
    price = deque(prices)
    
    while price:
        result = []        
        n = price.popleft()
        
        for i in price:
            result.append(i)
            if n > i:
                break
        
        answer.append(len(result))
        
    return answer

print(solution(answers))
