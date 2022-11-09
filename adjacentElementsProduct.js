// Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

// Example

// For inputArray = [3, 6, -2, -5, 7, 3], the output should be
// solution(inputArray) = 21.

// 7 and 3 produce the largest product.

function solution(inputArray) {
    let arr = []
    
    for(let i = 1; i < inputArray.length; i++) {
        let calc = inputArray[i] * inputArray[i-1]
        arr.push(calc)
    }
    
    return Math.max(...arr)
}