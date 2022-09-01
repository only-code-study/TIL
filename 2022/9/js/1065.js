let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
// let input = fs.readFileSync('ex.txt').toString().split(' ');

let result = 0;
for (let i = 1; i <= input[0]; i += 1) {
    let splitedNum = i.toString().split('')
    let prev = -1;
    let gap = 1000;
    let re = true;
    for (let a = 0; a < splitedNum.length; a += 1) {
        if (prev == -1) {
            prev = parseInt(splitedNum[a]);
            continue;
        }
        if (gap == 1000) {
            gap = prev - parseInt(splitedNum[a]);
            prev = parseInt(splitedNum[a]);
            continue;
        }
        if (gap != prev - parseInt(splitedNum[a])) {
            re = false;
            break;
        }
        prev = parseInt(splitedNum[a]);
    }
    if (re) {
        // console.log(i, ' ', gap);
        result += 1;
    }
}

console.log(result)
