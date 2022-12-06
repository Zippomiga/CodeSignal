// You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

// Example

// For inputArray = [1, 1, 1], the output should be
// solution(inputArray) = 3.


function solution(arr) {
    let minMoves = 0
    
    for(let i = 1; i < arr.length; i++) {
        if(arr[i] <= arr[i-1]) {
            let diff = arr[i-1] - arr[i] +1
            arr[i] += diff
            minMoves += diff
        }
    }
    
    return minMoves
}