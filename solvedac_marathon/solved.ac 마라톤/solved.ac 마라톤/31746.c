#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	char word1[11] = "SciComLove";
	char word2[11] = "evoLmoCicS";

	int n;

	scanf("%d", &n);
	if (n%2 == 1) {
		printf("%s", word2);
	}
	else {
		printf("%s", word1);
	}


	return 0;
}