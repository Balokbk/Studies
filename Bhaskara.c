#include<stdio.h>
#include<math.h>

float funDelta(float nA, float nB, float nC){
    float quadB, quatroAC, resultadoDelta;
    quadB = nB * nB;
    quatroAC = 4 * nA * nC;
    resultadoDelta = quadB - quatroAC;
    return(resultadoDelta);
};
float funBhaskaraPos(float delta, float nA, float nB){
    float resultadoBhaskara, menosB, div;
    menosB = -nB + sqrt(delta);
    div = menosB / (nA * 2);
    resultadoBhaskara = div;
    return (resultadoBhaskara);
};
float funBhaskaraNeg(float delta, float nA, float nB){
    float resultadoBhaskara, menosB, div;
    menosB = -nB - sqrt(delta);
    div = menosB / (nA * 2);
    resultadoBhaskara = div;
    return (resultadoBhaskara);
};

int main(){
    //definindo as variáveis
    float a, b, c, delta, resultPos, resultNeg;
    printf("Digite 3 números, sendo a, b, c, respectivamente\n");
    scanf("%f %f %f", &a, &b, &c);
    delta = funDelta(a, b ,c);
    printf("Calcularemos o Delta, que é b^2 - 4ac\n Delta = %0.f^2 - 4*%0.f*%0.f\nDelta = %0.f\n", b, a, c, delta);
    if(delta<0){
        printf("Delta negativo, não há raiz!\n");
        return main();
    }
    else{
        printf("Agora calcularemos (-B^2 +/- sqrt(Delta))/2\n");
        resultPos = funBhaskaraPos(delta, a, b);
        resultNeg = funBhaskaraNeg(delta, a, b);
        printf("O resultado X positivo é: %0.f\nO resultado X negativo é: %0.f\n", resultPos, resultNeg);
    }
    return 0;
}