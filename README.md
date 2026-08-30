# optimized-countdown-numbers-solver

# Project objective:

Program which solves the Countdown numbers game as fast as possible, but by computing solutions on-the-fly without relying on any pre-computation

# Building the cpp implementation to be used by Python:

g++ -O3 -shared -fPIC -std=c++17 src/countdown/solver.cpp -o build/libcountdown.so

# Building the cpp implementation for debugging:

g++ -g src/countdown/main.cpp src/countdown/solver.cpp -o build/countdown_app