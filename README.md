# optimized-countdown-numbers-solver

# Project objective:

Program which solves the Countdown numbers game as fast as possible, but by computing solutions on-the-fly without relying on any pre-computation

# Building the cpp implementation:

g++ -O3 -shared -fPIC -std=c++17 src/countdown/solver.cpp -o build/libcountdown.so