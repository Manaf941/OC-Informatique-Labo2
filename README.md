> https://github.com/Manaf941/OC-Informatique-Labo2

# exo1
This script draws the belgian and japanese flag with Turtle.
![exo1 screenshot](https://i.le-bunker.ch/HqUTJhy9.png)

# exo2
This script draws a chessboard with Turtle
![exo2 screenshot](https://i.le-bunker.ch/FQNaM6Kq.png)

# exo3
This script computes all prime numbers between 1 and 300, and displays them in the terminal.
![exo3 screenshot](https://i.le-bunker.ch/NpFQVthk.png)

# exo4
This script simulates heads or tails, and displays the result in the terminal. The user can input a desired number of games. 

As Python is pretty slow for this kind of task, I've made an optimized version in python that computes multiples games at once, another one in JavaScript, and another one in Rust. The goal of those three optimized versions were to compare the different execution times between the different programming languages, and also what simple optimizations could have been made to the initial task to make it faster. My most optimized version could compute 9662x faster than the initial Python one

![exo4 screenshot](https://i.le-bunker.ch/PCNQnCrO.png)

## Benchmark
These benchmark were ran on my MacBook Pro M1 2021 on Sonoma.

| Implementation       	| Throws       	| Time             	| % faster than Python 	|
|----------------------	|--------------	|------------------	|----------------------	|
| Python3.11 Randint   	| 100 millions 	| 39.69151 seconds 	| N/A                  	|
| Python3.11 Optimized 	| 100 millions 	| 6.592989 seconds 	| 502.0260%            	|
| JavaScript (bun)     	| 100 millions 	| 0.145771 seconds 	| 27128.6737%          	|
| Rust                 	| 100 millions 	| 0.004820 seconds 	| 823211.6737%         	|
| Rust                 	| 100 billions 	| 4.107171 seconds 	| 966295.3606%         	|