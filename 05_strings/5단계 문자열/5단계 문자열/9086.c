#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main(void) {

	char word[1000];
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%s", word);
		printf("%c%c\n", word[0], word[(int)strlen(word) - 1]);
	}

	return 0;
}