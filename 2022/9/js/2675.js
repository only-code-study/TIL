const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
// const input = fs.readFileSync("ex.txt").toString().split("\n");

for (let i = 1; i <= parseInt(input[0]); i++) {
  let [count, value] = input[i].split(" ");
  let result = "";
  for (let v of value.split("")) {
    result += Array.from({ length: count })
      .map(() => v)
      .join("");
  }
  console.log(result);
}
