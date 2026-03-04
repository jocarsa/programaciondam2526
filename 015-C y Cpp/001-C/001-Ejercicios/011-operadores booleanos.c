#include <stdio.h>

int main(){
	int escierto = 4 == 4 && 3 == 3 && 2 == 2;
	printf("%i",escierto);
  int escierto2 = 4 == 4 && 3 == 3 && 2 == 1;
	printf("%i",escierto2);
  
  escierto = 4 == 4 || 3 == 3 || 2 == 2;
	printf("%i",escierto);
  
  escierto = 4 == 4 || 3 == 3 || 2 == 1;
	printf("%i",escierto);
  
  escierto = 4 == 4 || 3 == 2 || 2 == 1;
	printf("%i",escierto);
  
  escierto = 4 == 3 || 3 == 2 || 2 == 1;
	printf("%i",escierto);
  return 1;
}