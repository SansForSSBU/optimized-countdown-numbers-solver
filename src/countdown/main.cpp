#include <array>

extern "C" {
    int solve_countdown(const std::array<int, 6>& numbers, int target);
}

int main() {
    std::array<int, 6> nums = {25, 50, 3, 8, 1};
    int target = 387;
    solve_countdown(nums, target);
    return 0;
}