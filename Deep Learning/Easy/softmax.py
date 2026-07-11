import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score=max(scores)
    exp_list=[math.exp(score-max_score) for score in scores]
    
    total=sum(exp_list)

    result=[]
    for softmax in exp_list:
        result.append(softmax/total)
    
    return result



        