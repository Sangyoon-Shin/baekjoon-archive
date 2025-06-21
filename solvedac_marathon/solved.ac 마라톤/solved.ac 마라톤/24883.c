#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>


int main(void) {

	char word[2];

	scanf("%s", &word);

	char string1[2] = "n";
	char string2[2] = "N";

	if (strcmp(word, string1) == 0 || strcmp(word, string2)==0){
		printf("Naver D2");
	}
	else {
		printf("Naver Whale");
	}


	return 0;
}
