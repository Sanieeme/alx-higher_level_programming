#!/usr/bin/node
const size = process.argv[2];
if (isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  const Size = parseInt(size);
  for (let i = 0; i < Size; i++) {
    let r = '';
    for (let j = 0; j < Size; j++) {
      r += 'X';
    }
    console.log(r);
  }
}
