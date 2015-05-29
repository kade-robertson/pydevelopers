# pydevelopers - Developers interpreter in Python
A Python interpreter for the Developers programming language

Developers is a joke language that parodies an incident at a Microsoft Developer's conference where Steve Ballmer is supposed to have chanted the word developers at least 14 times in a row. It is basically Brainfuck with a few extensions. It appeared briefly in the Wikipedia in the beginning of 2006, but it has not reappeared anywhere since its deletion. [[source](https://esolangs.org/wiki/Developers)]

Simply does Developers -> BF -> Python

| Key          | BF Equiv | C Equiv         |
|--------------|----------|-----------------|
| Developers   | +        | ++*ptr;         |
| Developers*2 | -        | --*ptr;         |
| Developers*3 | >        | ++ptr;          |
| Developers*4 | <        | --ptr;          |
| Developers*5 | ,        | *ptr=getchar(): |
| Developers*6 | .        | putchar(*prt);  |
| Developers*7 | [        | while (*ptr) {  |
| Developers*8 | ]        | }               |

# Usage
```
python pydevelopers file.dev
```
