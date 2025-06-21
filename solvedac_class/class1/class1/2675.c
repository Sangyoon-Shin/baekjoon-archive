#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {

	int n, r;

	char word[20];

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d %s", &r, word);

		for (int j = 0; j < (int)strlen(word); j++) {
			for (int k = 0; k < r; k++) {
				printf("%c", word[j]);
			}
		}
		printf("\n");
	}


	return 0;
}