// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
input = ['3', '0 0 13 40 0 37', '0 0 3 0 7 4', '1 1 1 1 1 5'];
input.splice(0, 1);
let x1, y1, r1, x2, y2, r2, dist;

for (data of input) {
    [x1, y1, r1, x2, y2, r2] = data.split(' ').map(Number);
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2;
    if (dist == 0 && r1 == r2) {
        console.log(-1);
    } else if (dist == (r1 + r2) ** 2 || dist == (r1 - r2) ** 2) {
        console.log(1);
    } else if (dist < (r1 + r2) ** 2 && dist > (r1 - r2) ** 2) {
        console.log(2);
    } else {
        console.log(0);
    }
}
