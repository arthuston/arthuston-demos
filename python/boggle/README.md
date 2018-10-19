# boggle
Boggle puzzle game.
Find words in a grid, according to the following rules: The letters must be adjoining in a 'chain'.
Letters in the chain may be adjacent horizontally, vertically, or diagonally. The letter position cannot be used
more than once in the chain.

This reads the puzzle and list of words from stdin. Example usage:
cat input.txt | python boggle.py

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

The sample input will find dog in the first line, cat in lines 1-2, bird in lines 2-3, mouse in lines 3-4, and gerbil
twice on lines 4-5. deer will not be found.
