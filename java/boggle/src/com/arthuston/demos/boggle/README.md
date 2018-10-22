# boggle
Boggle puzzle game.
Find words in a grid, according to the following rules: The letters must be adjoining in a 'chain'.
Letters in the chain may be adjacent horizontally, vertically, or diagonally. The letter position cannot be used
more than once in the chain.

This reads the puzzle and list of words from stdin.

Sample input:
5 <br />
dogca <br />
ebirt <br />
rxxdm <br />
gesuo <br />
erbil <br />
6 <br />
dog <br />
cat <br />
deer <br />
bird <br />
gerbil <br />
mouse <br />

Sample output:<br />
dog<br />
deer<br />
cat<br />
bee<br />
bird<br />
bee<br />
bee<br />
mouse<br />
mouse<br />
gerbil<br />
gerbil<br />
bee<br />
bee<br />

The sample output returns dog, deer and cat starting at line 1, bee (three times) and bird starting at line 2,
mouse (twice) starting at line 3, gerbil (twice) starting at line 4, and bee (twice) starting at line 5.
