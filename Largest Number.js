// Given an integer n, return the largest number that contains exactly n digits.

// Example

// For n = 2, the output should be
// solution(n) = 99.

function solution(n) {
    let largest = ''
    
    while(n > 0) {
        largest += '9'
        n--
    }
    
    return Number(largest)
}

// <--------------- Others --------------->

function solution(n) {
    return Number('9'.repeat(n))
}