#include <stdio.h>

int main() {
    const char baseDigits[16] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
    int convertedNum[64];
    long int numToConvert, fixedNum;
    int nextDigit, base, i = 0;

    fixedNum = numToConvert;
    //Receives the number and base.
    printf("Insert a number and choose the base (2, 8 or 16).\n");
    scanf("%ld %d", &numToConvert, &base);

    if(base == 2 || base == 8 ||base == 16){
    //Converts the number to the base we selected.

    do{
        convertedNum[i] = numToConvert % base;
        i++;
        numToConvert = numToConvert / base;
        }
    while (numToConvert !=0);

    //Shows the number in the inverse order.  

    printf("Converted number %ld to base %d = ", fixedNum, base);
    for(i--; i >= 0; i--){
        nextDigit = convertedNum[i];
        printf("%c\n", baseDigits[nextDigit]);
    }
    }
    else{
        printf("Use other base(2, 8 or 16)!\n");
    }
    return 0;
}
