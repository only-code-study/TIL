let allNumber = []

const callNext = (number) => {
    let nextNumber = number;
    let tempNumber = number;

    do {
        nextNumber += tempNumber % 10
        tempNumber = Math.floor(tempNumber / 10)
    } while(tempNumber != 0)

    if (nextNumber != number) {
        allNumber.push(nextNumber);
    }

    if (allNumber.includes(number)) {
        allNumber = allNumber.filter( d => d != number);
        return false
    }
    return true;
}

for (let i = 1; i < 10000; i += 1) {
    if(callNext(i)) {
        console.log(i);
    }
}