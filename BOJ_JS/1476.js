// 백준 NodeJS로 풀 시 메모리초과 발생

let E, S, M;
// [E, S, M] = require('fs').readFileSync('/dev/stdin').toString().split(' ')
[E, S, M] = [15, 28, 19];

let answer = S;

while (true) {
    if ((answer - E) % 15 == 0 && (answer - M) % 19 == 0) {
        break;
    }
    answer += 28;
}

console.log(answer);
