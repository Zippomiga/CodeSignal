// You are given a two-digit integer n. Return the sum of its digits.

// Example

// For n = 29, the output should be
// solution(n) = 11.


function solution(n) {
    const split = String(n).split('')
    
    return Number(split[0]) + Number(split[1])
}