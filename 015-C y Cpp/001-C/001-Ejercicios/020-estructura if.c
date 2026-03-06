#include <stdio.h>

int main(){
	int edad = 47;
  if(edad < 10){
  	printf("Eres un niño \n");
  }else if(edad < 20 && edad >=10){
  	printf("Eres un adolescente \n");
  }else if(edad < 30 && edad >=20){
  	printf("Eres un joven \n");
  }else if(edad >=30){
  	printf("Ya no eres un joven \n");
  }else{
  	printf("Lo que has introducido no es una edad \n");
  }
  return 0;
}