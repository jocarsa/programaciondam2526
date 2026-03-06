#include <stdio.h>
#include <time.h>

int main(){

    clock_t inicio, fin;			// Declaramos variables de tipo reloj
    double tiempo;						// Doble quiere decir doble precision

    inicio = clock();					// Mide el tiempo al inicio

    float numero = 1.0000000432;	// Declara un numero
    int contador;								// Declara un contador

    for(contador = 0; contador <= 235324543; contador++){
        numero = numero * 1.00000000645;
    } // Bucle for que lo multiplica muchas veces

    fin = clock();						// Medimos el tiempo al final

    tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;	// Sacamos el diferencial

    printf("El resultado es: %f\n", numero);	// Y lo ponemos en pantalla
    printf("Tiempo de ejecucion: %f segundos\n", tiempo);

    return 0;
}