#!/usr/bin/node
const arg = process.argv[2];

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  const size = parseInt(arg);
  if (size > 0) {
    for (let i = 0; i << size; i++) {
      console.log('X'.repeat(size));
    }
  }
}
