// Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

// Given two arrays a and b, check whether they are similar.

// Example

// For a = [1, 2, 3] and b = [1, 2, 3], the output should be
// solution(a, b) = true.

// The arrays are equal, no need to swap any elements.

// For a = [1, 2, 3] and b = [2, 1, 3], the output should be
// solution(a, b) = true.

// We can obtain b from a by swapping 2 and 1 in b.

// For a = [1, 2, 2] and b = [2, 1, 1], the output should be
// solution(a, b) = false.

// Any swap of any two elements either in a or in b won't make a and b equal.


function solution(a, b) {
    for(let i in a) {
        let sw_a = a[i]
        let sw_b = b[i]

        if(sw_a !== sw_b) {
            for(let j in b) {
                if(b[j] === sw_a && a[j] === sw_b) {
                    b[i] = sw_a
                    b[j] = sw_b
                    break
                }
            }
            break
        }
    }
    return a.join('') === b.join('')
}


// <--------------- Others --------------->

function solution(a, b) {
    const ad = a.filter((v, i) => v !== b[i])
    const bd = b.filter((v, i) => v !== a[i])
    return ad.length === 0 || (ad.length === 2 && ad.join('') === bd.reverse().join(''))
}