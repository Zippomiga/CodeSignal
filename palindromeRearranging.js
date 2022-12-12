// Given a string, find out if its characters can be rearranged to form a palindrome.

// Example

// For inputString = "aabb", the output should be
// solution(inputString) = true.

// We can rearrange "aabb" to make "abba", which is a palindrome.


function solution(s) {
	const freq = {}

	for(const ch of s) {
		freq[ch] = (freq[ch] || 0) + 1
	}
  
	let oddCount = 0

	for(const count of Object.values(freq)) {
		if(count % 2 === 1) {
		oddCount++
		}
	}
  
	return oddCount <= 1
}

//Above, a code made by ChatGPT. Below, by me, but it passes 18/20 tests :(


function solution(s) {
	let S = [...s].sort().join('')

	for(let i = 0; i <= S.length; i+=2) {
		if(S[i+1] === undefined || i >= S.length) {
			console.log('Jesus')
			return true
		}

		if(S[i+1] !== S[i]) {
			console.log('Satanas')
			return false
		}
	}
}