# An Investigation into Generic Algorithms and their Implementations

|               |                       |
|---------------|-----------------------|
|   Author      |   Ethan Tan Wee En    |
|   Language    |   Python (py)         |
|   Date        |   August 2021         |

## Fibonacci Sequence

Directory: `fibonacci`

3 algorithms are used to evaluate the fibonacci progression at any ![](https://render.githubusercontent.com/render/math?math=n\in\N) position:
1.  Recursive Algorithm
2.  Dynamic Programming
3.  Formula (![](https://render.githubusercontent.com/render/math?math=\frac{\phi^n}{\sqrt{5}}))

Here are the differences in the algorithms:

![](fibonacci/assets/rec-dyn-form.png)

1.  Recursive Algorithm:
    *   Time Complexity: O(fib(n))
    *   Space Complexity: O(fib(n))

![](fibonacci/assets/dyn-form.png)

2.  Dynamic Programming Algorithm:
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)

![](fibonacci/assets/form.png)

3.  Formulaic Algorithm:
    *   Time Complexity: O(1)
    *   Space Complexity: O(1) (0)

## Sorting Algorithms

Directory: `sorting`

## Tower of Hanoi

Directory: `tower_of_hanoi`

Minimal number of moves (basic): 2<sup>n</sup> - 1 <br/>
Minimal number of moves (constrained): 3<sup>n</sup> - 1

## References
