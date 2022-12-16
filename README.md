# Return expected key presses for a multi-press keypad
https://en.wikipedia.org/wiki/Telephone_keypad#/media/File:Telephone-keypad2.svg
-------------------------
|       |  ABC  |  DEF  |
|   1   |   2   |   3   |
-------------------------
|  GHI  |  JKL  |  MNO  |
|   4   |   5   |   6   |
-------------------------
| PQRS  |  TUV  | WXYZ  |
|   7   |   8   |   9   |
-------------------------
|       |       |       |
|   *   |   0   |   #   |
-------------------------

Given a word, output the string of keypresses required.  Press a key multiple times to access the desired character e.g. to insert a B press 22.

In order to insert two characters in sequence from the same key, the user must pause before pressing the key a second time. The space character ' ' should be printed to indicate a pause. For example, `2 2` indicates AA whereas `22` indicates B.

# Examples:

go -> 4666
go go -> 466604666
no -> 66 666

# Test cases are included.  Run all test cases as:

python keys.py

or particular example as:

python keys.py <word>
