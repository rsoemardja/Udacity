Nested Loops

Nested are loops within loops

We need Nested to added some complexity/condition for the loops that we have provided

Examples

for (var x = 0; x < 5; x = x + 1) {
  for (var y = 0; y < 3; y = y + 1) {
    console.log(x + "," + y);
  }
}

What it will print out
0,0
0,1
0,2 (up to 4,2)
1,1
1,2

Notice that the output will be display in that order it will cycle from the x loop to the y loop.

Example 2
for (var i = 0; i <= 6; i = i + 2) {
  console.log(i);
}

What will print out
0 2 4 6
The logic behind it
0 + 2 = 2
2 + 2 = 4
4 + 2 = 6
6 + 2 = 8 (8 > 6, so loop exits)