# N<sup>th</sup> Term of Fibonacci Sequence

A simple and light-weight webpage where the user inputs an integer N and obtains the n<sup>th</sup> term of the Fibonacci sequence. The Fibonacci Sequence is a series of numbers where each number is the sum of the last two numbers, starting with 1 and 1. F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub>

### Test Cases handled:
Calculates values that are way greater than Number.MAX_SAFE_INTEGER i.e. 9007199254740991 in JavaScipt (e.g. where N > 10000) using BigInt.
### References:
* [Fibonacci Sequence](https://www.mathsisfun.com/numbers/fibonacci-sequence.html)


There are several ways to optimize for high load including use of all CPU cores like using Redis, etc. But I introduced one single formula to get nth term of Fibonacci sequence, so in this case, the O(1) time complexity formula for Fibonacci calculation would be more efficient than using a caching mechanism like Redis or Memcached. The caching would add additional overhead that would likely outweigh the benefits for this specific problem.