#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

#if 0
int main(void) {

	char word[101];

	scanf("%s", word);
	printf("%d", strlen(word));

	return 0;
}
#endif

int main(void) {

	char word[101];
	int count = 0;

	scanf("%s", word);
	for (int i = 0; i < (int)strlen(word); i++) { // strlen�� size_tŸ��. ��ȣ���� ����. i�� size_t�� ���ų�, strlen�� Ÿ��ĳ���� ���ֱ�
		if (word[i] != '\0') { // ""�� ���ڿ�, ''�� ���� ���ͷ�. ""�� ����ϸ� const char* ������ �ǹǷ�, word[i]�� �ǹ��ϴ� char Ÿ�԰��� �񱳰� �ǹǷ� ����.
			count++;
		}
	}
	printf("%d", count);

	return 0;
}