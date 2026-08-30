#include <array>
#include <iostream>

extern "C" {
    int solve_countdown(const std::array<int, 6>& numbers, int target)
    {
        for (int i=0; i<6; i++)
        {
            std::cout << numbers[i] << " ";
        }
        std::cout << "\n";
        std::cout << target << "\n";
        return 0;
    }
}