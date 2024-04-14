# CMPS 2200 Assignment 3
## Answers

**Name:**_________________________


Place all written answers from `assignment-03.md` here for easier grading.

1a). Initialize an empty list to hold the coins chosen. Find the largest coin denomination that does not exceed N. This is done by finding the highest power of 2 (2^k) that is less than or equal to N. Add this coin to the list of chosen coins. Subtract the value of the chosen coin from N to get the new value of N. Repeat steps 2 through 4 until IN becomes O. Return the list of chosen coins.

1b). The optimality of the greedy algorithm for converting an amount N into the fewest number of coins with denominations that are powers of 2 is proven through the greedy choice and optimal substructure properties. The greedy choice property is satisfied because selecting the largest denomination that does not exceed N at each step is equivalent to flipping the highest unset bit in N's binary representation to 1, ensuring that each choice is locally optimal and contributes to the global optimum. The optimal substructure property holds because the problem, once reduced by the greedy choice (subtracting the selected coin's value from M), remains the same problem but with a smaller amount, N'. Since any integer amount can be uniquely represented as a sum of powers of 2, making the greedy choice at each step guarantees an optimal solution by systematically covering the largest part of N with each coin selected, thereby ensuring that the solution to the
overall problem includes optimal solutions to its sub-problems.

1c). Given that the denominations are powers of 2, the greedy algorithm for making change in Geometrica exhibits both work and span complexities of O(log N). This efficiency stems from the fact that each coin selection substantially reduces the remaining amount to be converted, often by half or more, limiting the number of iterations (and thus operations) needed to reach the final solution.

2a). In Fortuito, where coin denominations are arbitrary and not limited to powers of 2, the greedy algorithm for making change can fail to produce the minimum number of coins. For example, with denominations of 1, 3, and 4, the greedy algorithm would suggest making change for 6 with coins of 4, 1, 1, totaling three coins. However, the optimal solution is to use two 3 coins, totaling just two coins. This illustrates the failure of the greedy algorithm in situations with arbitrary denominations, as it doesn't always yield the fewest coins due to its inherent reliance on making the largest denomination choice at each step, which isn't always optimal outside the structured oinary-like svstem of nowers of 2 found in Geometrica

2b). The coin change problem in Fortuito, with its arbitrary denominations, retains the optimal substructure property essential for dynamic programming approaches. This property signifies that an optimal solution to making change for any amount N contains within it optimal solutions for smaller subsets of N. For example, if the best way to change N includes a coin of denomination d, then the solution for the remaining amount N - d is also optimal. Dynamic programming exploits this by breaking the problem into smaller sub-problems, ensuring that each step towards solving for N is informed by the optimal solutions of these sub-problems, unlike the greedy method that may overlook these due to its linear largest-first approach

2c). In addressing the coin change problem for Fortuito's arbitrary denominations through dynamic programming, we construct a solution that leverages the optimal substructure property by iteratively calculating the minimum number of coins needed for all amounts up to N. Initializing an array 'minCoins' to track the minimum coins required for each sub-amount, we iterate from 1 to N, updating 'minCoins[i]' by considering each coin denomination Dj and choosing the best option that minimizes the coin count. This approach, with a work complexity of O (N x k) where k is the number of denominations, and a span complexity of O (N), systematically builds up from the base case, ensuring each sub-problem is optimally solved before it contributes to solving larger amounts, thus efficiently determining the fewest coins needed for any amount N in Fortuito's system.



