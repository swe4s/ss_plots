#A set of stupid simple plots.

## scatter plot
The scatter plot can take files in three formats

### One column: Y
```
python scatter.py --in_file rand_1_col.txt --out_file s_just_y.png --x_label 'Non rand' --y_label 'Rand'
```

`rand_1_col.txt`
```
8119
9794
16494
18926
19529
17858
14104
29539
20705
```

`s_just_y.png`
<img src="/imgs/s_just_y.png" width="100%"/>

### Two column: X Y
```
python scatter.py --in_file rand_2_col.txt --out_file s_x_and_y.png --x_label 'Rand' --y_label 'Rand'
```

`rand_2_col.txt`
```
22657 31381
20517 2750
16498 16717
7618 28447
20515 11879
23737 10329
12389 25019
12338 9602
13504 30283
25754 30543
```

`s_x_and_y.png`
<img src="/imgs/s_x_and_y.png" width="100%"/>

### Three column: Name X Y
```
python scatter.py --in_file rand_3_col.txt --out_file s_x_y_and_name.png --x_label 'Rand' --y_label 'Rand'
```

`rand_3_col.txt`
```
A 4701 24692
B 26337 1467
C 18576 22038
D 13297 15634
E 28235 2460
F 29150 13147
G 31944 31946
H 13843 11331
I 29970 8133
J 24093 32527
```

`s_x_y_and_name.png`
<img src="/imgs/s_x_y_and_name.png" width="100%"/>

## box plot
The box plotter takes files where each line is the box name followed by numerical values
```
python box.py --in_file rand_10_x_10.txt --out_file b_rand.png --x_label 'Rand' --y_label 'Rand'
```

`rand_10_x_10.txt`
```
A 2400 29221 30235 22660 20760 32197 32614 26864 23955 32268
B 29190 29070 7030 5011 31443 15199 937 15439 4082 15435
C 31699 12375 7086 24269 17048 16243 30993 6238 25490 31592
D 7750 31394 28432 15110 4270 11093 29073 16877 32452 28404
E 26367 6435 7089 12843 9643 25688 6318 15874 32012 16371
F 22558 710 1079 29668 13927 9656 21534 1833 1172 15736
G 10632 29 4268 26927 10964 23939 22480 11903 19821 5206
H 15894 18988 5900 7758 26664 24455 14001 25906 4765 12958
I 12639 5857 787 22821 7834 11806 28432 3618 12449 15390
J 29854 5212 1132 16083 160 21377 30052 4087 16118 7194
```

`b_rand.png`
<img src="/imgs/b_rand.png" width="100%"/>

## histogram
The histogram plotter takes files with one numberical value per line.

```
python histogram.py --in_file rand_1_col.txt --out_file h_rand.png --x_label 'Rand' --y_label 'Freq'
```

`rand_1_col_1000.txt`
```
2938
89
0
25795
29207
12525
11755
7450
22034
1710
...
```

`h_rand.png`
<img src="/imgs/h_rand.png" width="100%"/>
