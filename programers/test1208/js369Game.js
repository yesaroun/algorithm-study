function solution(order) {
    var answer = 0;

	order = String(order);

	for (let i=0; i<order.length; i++) {
		if (order[i] == "3" || order[i] == "6" || order[i] == "9") {
			answer += 1;
		}
	}

    return answer;
}

console.log(solution(3))
console.log(solution(29423))

