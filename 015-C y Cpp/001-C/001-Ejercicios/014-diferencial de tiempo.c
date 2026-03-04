#include <stdio.h>
#include <time.h>

int main(){

    clock_t inicio, fin;
    double tiempo;

    inicio = clock();

    float numero = 1.0000000432;
    int contador;

    for(contador = 0; contador <= 235324543; contador++){
        numero = numero * 1.00000000645;
    }

    fin = clock();

    tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("El resultado es: %f\n", numero);
    printf("Tiempo de ejecucion: %f segundos\n", tiempo);

    return 0;
}