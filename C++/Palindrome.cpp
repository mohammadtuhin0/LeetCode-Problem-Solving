#include <iostream>
using namespace std;
int palindrome(int num){
    int originalNum = num;
    int reverse =0;

    while(num != 0){
        int lastNum = num % 10;
        reverse = reverse * 10 + lastNum;
        num = num / 10;
    }
    return originalNum == reverse;
}
int main() {
    int n;
    cout<<"Enter numbers : ";
    cin>>n;
    if(palindrome(n)){
        cout<<"Palindrome Number ";
    } else {
        cout<<"Not Palindrome Number ";
    }
}