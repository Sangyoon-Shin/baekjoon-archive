#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	char str[101];
	scanf("%s", str);

	int len = strlen(str);

	int start = 0;
	int end = len - 1;
	int flag = 1;

	while (start < end) {
		if (str[start] != str[end]) {
			flag = 0;
			break;
		}
		start++;
		end--;
	}

	if (flag == 0) {
		printf("0");
	}
	else {
		printf("1");
	}

	return 0;
}