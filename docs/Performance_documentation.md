## Performance test for A*
Path lenght is always maximum
- size 20*20 mean 98.6861 (1.0)
- size 40*40 mean 220.7928 (2.24)
- size 80*80 mean 500.2186 (5.07)
- size 160*160 mean 1,164.0914 (11.80)

$\color{green}{\text{Performance is acceptable}}$

## Performance test for prims
Connections in the test graph is the maximum amount.
- Points 100 mean 245.9441 (2.49)
- Points 200 mean 559.5618 (5.67)
- Points 400 mean 1,260.4896 (12.77)
- Points 800 mean 2,825.7610 (28.63)

$\color{green}{\text{Performance is acceptable}}$

## Performance test for Bowyer_watson
- Points 100 mean 6,852.8290 (69.44)
- Points 200 mean 25,624.3211 (259.65)
- Points 300 mean 60,811.3000 (616.21)
- Points 400 mean 02,876.8300 (>1000.0)

$\color{red}{\text{Performance is unacceptable}}$

Bowyer_watson algorithm seems to run on N^2 time.
This can be seen because the time increase isnt even close to being linear.(nlogn isnt linear but it would be much closer)

- I was told by the course organizer that N^2 time is acceptable for this course. I wont edit this further.
# Tests done 14.02.2026 Time 16:55 Edited at 16.02.2026


## Performance test for A* with added terrain checking.
Path lenght is always maximum
test_a_star[20]                 409.3170 (1.09)
test_a_star[40]               1,743.4972 (4.64)
test_a_star[80]               7,394.2774 (19.69)
test_a_star[160]             31,194.8688 (83.06)
runs about at O(S^2)
S = 20,...,160
With the added weight checking the A* algorithm needed alot of optimization.
First i wanted to have the grid functions be used but this was a bad idea.
Performance fixes:
- Python requires overhead when calling functions recreated functions in A*.
- I switched from numpy which is slower than math when not using arrays.
- Switched from euclidian to manhattan because it avoids expensive sqrt. And since i only move in 4 directions its an acceptable heuristic.
Normally many of these wouldnt be important but since i call these many times it adds up.

$\color{green}{\text{Performance is acceptable}}$

## Performance test for prims
Connections in the test graph is the maximum amount.
test_prims[100]                 375.5854 (1.0)
test_prims[200]                 800.8028 (2.13)
test_prims[400]               1,803.4187 (4.80)
test_prims[800]               3,994.4695 (10.64)
About O(N)
N = 100,...,800
Prims is largely unchanged. 
$\color{green}{\text{Performance is acceptable}}$

## Performance test for Bowyer_watson
test_b_w_benchmark[100]       6,600.7917 (17.57)
test_b_w_benchmark[200]      25,643.0615 (68.27)
test_b_w_benchmark[300]      62,383.0647 (166.10)
test_b_w_benchmark[400]     103,794.4000 (276.35)
About O(N^2)
N = 100,...,400
$\color{green}{\text{Performance is acceptable}}$
Bowyer watson is unchanged.
Bowyer_watson algorithm seems to run on N^2 time. I was told that this is an acceptable time for this course.

# Tests done 17.02.2026 Time 00.23