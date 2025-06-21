#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {

	char word[9];

	char string1[9] = "fdsajkl;";
	char string2[9] = "jkl;fdsa";

	char string3[9] = "asdf;lkj";
	char string4[9] = ";lkjasdf";

	char string5[9] = "asdfjkl;";

	char string6[9] = ";lkjfdsa";

	scanf("%s", word);

	if (strcmp(word, string1) == 0 || strcmp(word, string2) == 0) {
		printf("in-out");
	}
	else if (strcmp(word, string3) == 0 || strcmp(word, string4) == 0) {
		printf("out-in");
	}
	else if (strcmp(word, string5) == 0) {
		printf("stairs");
	}
	else if (strcmp(word, string6) == 0) {
		printf("reverse");
	}
	else {
		printf("molu");
	}

	return 0;
}

