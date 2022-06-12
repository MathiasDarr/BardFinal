let input = " JavaScript " ;
let output = "<div> + input.trim()" + "</div>"

const trim = str => str.trim();
const wrapInDiv = str => `<div>${str}</div>`;
const results = wrapInDiv(trim(input))
console.log(results)