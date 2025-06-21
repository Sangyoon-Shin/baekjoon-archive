#if 0
#define _CRT_SECURE_NO_WARNINGS	

#include <stdio.h>

int main(void) {
	int a, b;
	int num;
	int result[100000];

	scanf("%d", &num);

	for (int i = 0; i < num; i++) {
		scanf("%d %d", &a, &b);
		result[i] = a + b;
	}

	for (int i = 0; i < num; i++) {
		printf("%d\n", result[i]);
	}

	return 0;
}
#endif


#if 0
// 다른 풀이

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int A, B, T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{
		scanf("%d%d", &A, &B);
		printf("%d\n", A + B);
	}
	return 0;

}



#endif
