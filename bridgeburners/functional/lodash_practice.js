


import pkg from 'lodash/fp.js';
const { compose } = pkg;



const trim = str => str.trim();
const wrapInDiv = str => `<div>${str}</div>`;
const toLowerCase = str => str.toLowerCase();



const transform = compose(wrapInDiv, toLowerCase, trim )
console.log(transform("  aDFD df aDFF "))