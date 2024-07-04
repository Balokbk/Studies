#include <stdio.h>
int main(){
    int num, i, result;
    
    for(i=1;i<=10;i++){
        printf("Multiplication table: %d\n",i);
        for(num=1;num<=10;num++){
            result= i * num;
            printf("%d X %d = %d\n", i, num, result);
        }
    }
    
    return 0;
}