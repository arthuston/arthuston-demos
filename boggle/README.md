# boggle

Boggle puzzle game.
Given an X by Y grid of letters and a list of words, find all the words in the grid,
according to the following rules: The letters in each word must be adjacent to each other
in a 'chain' of letters and may be adjacent horizontally, vertically, or diagonally.
The letter position cannot be used more than once in a single word chain. The input is a
new-line delimited file containing the number of rows in the grid, the characters in each row,
the number of words to look for and the list of words, for example:

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

The program should find ```dog```, ```deer```, ```cat```, ```bee``` and ```bird``` as follows:

```
dog
```

```
d
e
re
```

```
  ca
   t
```

```
eb
 e
```

```
 bir
   d
```

The complete list of words should be:

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

[C++](boggle-cpp)<br/>
[Python](boggle-python)<br/>
[Java](boggle-java)
