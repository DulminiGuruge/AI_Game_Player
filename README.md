##     Implementing an AI Player with Alpha Beta Pruning  


Alpha Beta Pruning is a search algorithm used in game theory and decision trees, which efficiently explores game trees and eliminates branches that won't affect the final decision. This algorithm is particularly useful in games where there are two players, Maximizing Player who is trying to maximize their outcome and Minimizing Player is the other trying to minimize it. In this Tic Tac Toe game, the Maximizing Player is the AI and the algorithm alpha beta pruning is used maximize the chance of AI winning, while the Minimizing Player is the human opponent who is trying to minimize the AI's chances.

The algorithm of Alpha Beta Pruning is given below.

```
function minimax(node, depth, isMaximizingPlayer, alpha, beta):

    if node is a leaf node :
        return value of the node
    
    if isMaximizingPlayer :
        bestVal = -INFINITY 
        for each child node :
            value = minimax(node, depth+1, false, alpha, beta)
            bestVal = max( bestVal, value) 
            alpha = max( alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal

    else :
        bestVal = +INFINITY 
        for each child node :
            value = minimax(node, depth+1, true, alpha, beta)
            bestVal = min( bestVal, value) 
            beta = min( beta, bestVal)
            if beta <= alpha:
                break
        return bestVal

```



