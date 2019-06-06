# boggle

Boggle puzzle game.
Find words in a grid, according to the following rules: The letters must be adjoining in a 'chain'.
Letters in the chain may be adjacent horizontally, vertically, or diagonally. The letter position cannot be used
more than once in the chain.

Sample input:<br />
```
5
dogca
ebirt
rexdm
gesuo
erbil
7
dog
cat
deer
bird
gerbil
mouse
bee
```
Sample output:<br />
```
dog
deer
cat
bee
bird
bee
bee
mouse
mouse
gerbil
gerbil
bee
bee
```

The sample output returns dog, deer and cat starting at line 1, bee (three times) and bird starting at line 2,
mouse (twice) starting at line 3, gerbil (twice) starting at line 4, and bee (twice) starting at line 5.

[C++](boggle-cpp)<br/>
[Python](boggle-python)<br/>
[Java](boggle-java)
