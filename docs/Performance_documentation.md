## Performance test for A*
Path lenght is always maximum
- size 20*20 mean 98.6861 (1.0)
- size 40*40 mean 220.7928 (2.24)
- size 80*80 mean 500.2186 (5.07)
- size 160*160 mean 1,164.0914 (11.80)
$\color{green}{Performance is acceptable}$

## Performance test for prims
Connections in the test graph is the maximum amount.
- Points 100 mean 245.9441 (2.49)
- Points 200 mean 559.5618 (5.67)
- Points 400 mean 1,260.4896 (12.77)
- Points 800 mean 2,825.7610 (28.63)
$\color{green}{Performance is acceptable}$

## Performance test for Bowyer_watson
- Points 100 mean 6,852.8290 (69.44)
- Points 200 mean 25,624.3211 (259.65)
- Points 300 mean 60,811.3000 (616.21)
- Points 400 mean 02,876.8300 (>1000.0)

$\color{red}{Performance is unacceptable}$
Bowyer_watson algorithm seems to run on N^2 time.
This can be seen because the time increase isnt even close to being linear.(nlogn isnt linear but it would be much closer)

# Tests done 14.04.2026 Time 16:55