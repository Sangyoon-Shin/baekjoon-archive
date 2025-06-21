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
	for (int i = 0; i < (int)strlen(word); i++) { // strlen은 size_t타입. 부호없는 정수. i를 size_t로 놓거나, strlen을 타입캐스팅 해주기
		if (word[i] != '\0') { // ""는 문자열, ''는 문자 리터럴. ""를 사용하면 const char* 형식이 되므로, word[i]가 의미하는 char 타입과의 비교가 되므로 오류.
			count++;
		}
	}
	printf("%d", count);

	return 0;
}