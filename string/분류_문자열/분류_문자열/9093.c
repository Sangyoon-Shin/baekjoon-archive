#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	int n;
	char str[1001];
	scanf("%d ", &n); // �����̽��� �־���� enter Ű �Է¹޾Ƶ� ���� �Է¶� ���� ������־ ���� ����

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