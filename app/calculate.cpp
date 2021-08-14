#include <iostream>
#include "stdio.h"
using namespace std;


extern "C" int my_print(int a) {
        cout <<"Inside print";
        return 1;
    }

float calculate_avg(int* arr, int size) {
    int sum = 0;
    cout << size << endl;;
    for(int i = 0; i < size; i++) {
        cout << arr[i] << " ";
        sum = sum + arr[i];
    }
    return sum/size;

}

extern "C" int takeRange(int a, int b) {
        return a-b;
}


// int main() {
//     // int size = 5;
//     // int foo[5] = {1,2,3,4,5};
//     // float b = calculate_avg(foo,size);
//     cout << "Hello world";
//     return 0;
// }