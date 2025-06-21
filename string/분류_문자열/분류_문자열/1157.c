#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int findMost(char* str, int *alphabet) {

	while (*str != '\0') {
		if (*str >= 'a' && *str <= 'z') {
			alphabet[*str - 'a']++;
		}
		else if (*str >= 'A' && *str <= 'Z') {
			alphabet[*str - 'A']++;
		}
		str++;
	}

	int max = -1;
	char chmax = NULL;
	int flag = 0;
	for (int i = 0; i < 26; i++) {
		if (alphabet[i] > max && alphabet[i] > 0) {
			max = alphabet[i];
			flag = 0;
			chmax = i + 'A';
		}
		else if (alphabet[i] == max) {
			flag = 1;
		}
	}
	if (flag == 1) {
		printf("?");
	}
	else {
		printf("%c", chmax);
	}
}

int main() {

	char str[1000001];
	int alphabet[26] = { 0, };
	scanf("%s", str);

	findMost(str, alphabet);

	return 0;
}