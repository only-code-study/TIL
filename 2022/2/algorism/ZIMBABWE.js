const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

var inputs = [];
let count;

const init = (input) => {
    let e = input[0], m  = input[1]
    let c = countPerNumber(e);
    let r = countPerResult(e, m ,c, "");
}

const countPerNumber = (e) => {
    let counts = [];
    e.toString().split('').forEach(num => {
        if(counts[+num] === undefined) counts[+num] = 0;
        counts[+num] += 1;
    });
    return counts;
}

const countPerResult = (e, m, c, b) => {
    let result = 0;
    c.forEach((num, index) => {
        if (num !== 0) {
            c[index] -= 1;
            b += index;
            result += countPerResult(e, m, c, b);
            return result;
        }
        if (index = 10) {
            console.log(b);
            if ((+b < +e)||(+b / +c))
                return 1;
        }
    });
}

rl.on('line', (line) => {
    if(count === undefined) {
        count = +line;
    } else {
        inputs.push(line.trim().split(' '));
        count--;
    }
    if(count === 0) rl.close();
}).on('close', () => {
    inputs = inputs.reverse();
    let input;
    while(input = inputs.pop()) {
        init(input);
    }
});