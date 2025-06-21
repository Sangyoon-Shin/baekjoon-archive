#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	int n;
	char str[1001];
	scanf("%d ", &n); // 스페이스바 넣어줘야 enter 키 입력받아도 다음 입력때 버퍼 비어져있어서 오류 없음

	for (int k = 0; k < n;k++) {
		gets(str);
		char* sptr = str;
		char* wordptr = str;

		while (*sptr != '\0') {
			int len = 0;
			while ((*wordptr != ' ') && (*wordptr != '\0')) {
				wordptr++;
				len++;
			}
			sptr = wordptr;
			wordptr--;
			for (int i = 0; i < len; i++) {
				printf("%c", *wordptr);
				wordptr--;
			}
			printf(" ");
			wordptr = sptr + 1;
		}
		printf("\n");
	}

	return 0;
}