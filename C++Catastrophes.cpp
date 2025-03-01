#include <iostream>

class Bar {
public:
    int value;
};

int main() {
    Bar barArray[5];
    
    for (int i = 0; i < 5; ++i) {
        barArray[i].value = i;
    }

    for (int i = 0; i < 5; ++i) {
        Bar& thisBar = barArray[i];
        thisBar.value += 10; 
        std::cout << "Value of barArray[" << i << "]: " << thisBar.value << std::endl;
    }

    return 0;
}
