function solution(i, j, k) {
    var answer = 0;

	for (num=i; num<=j; num++) {
		var numStr = String(num);
		for (count=0; count<=numStr.length; count++){
			if (numStr[count] == String(k))
				answer += 1;
		}
	}

    return answer;
}

console.log(solution(1, 13, 1))
console.log(solution(3, 10, 2))
