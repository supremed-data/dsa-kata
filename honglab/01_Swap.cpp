#include <iostream>
using namespace std;

void MySwapPtr(int* i, int* j) {
    int temp = *i;
    *i = *j;
    *j = temp;
}

void MySwapRef(int& i, int& j) {
    int temp = i;
    i = j;
    j = temp;
}

bool CheckSorted(int a, int b) {
    return (a <= b);
}

int main() {
    {
        // Swap
        int a = 3;
        int b = 2;

        cout << a << " " << b << endl;

        MySwapPtr(&a, &b);
        
        cout << a << " " << b << endl;

        MySwapRef(a, b);

        cout << a << " " << b << endl;
    }

    {
        // Sorting
        int arr[] = { 4, 6 };

        cout << arr[0] << " " << arr[1] << endl;

        if (arr[0] >= arr[1]) {
            MySwapRef(arr[0], arr[1]);
        }

        cout << arr[0] << " " << arr[1] << endl;
    }

    int arr[2];

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            arr[0] = j;
            arr[1] = i;

            if (arr[0] >= arr[1]) {
                swap(arr[0], arr[1]);
            }

            cout << boolalpha;
            cout << arr[0] << " " << arr[1] << " "
            << CheckSorted(arr[0], arr[1]) << endl;
        }
    }

    return 0;
}
