#if 0
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {
	int a, b;
	scanf("%d", &a);
	scanf("%d", &b);
    int b3 = b / 100;
	int b2 = (b - (b3 * 100)) / 10;
	int b1 = b - ((b3 * 100) + (b2 * 10));
	int result3;
	int result4;
	int result5;

	result3 = a * b1;
	result4 = a * b2;
	result5 = a * b3;
	printf("%d\n", result3);
	printf("%d\n", result4);
	printf("%d\n", result5);
	printf("%d", a * b);

	return 0;
}
#endif


#if 0
step 10
int main() {
	int A, B;
	scanf("%d %d", &A, &B);
	int B1, B2, B3;
	B1 = B / 100;
	B2 = (B / 10) - (B1 * 10);
	B3 = B - B1 * 100 - B2 * 10;
	printf("%d\n%d\n%d\n%d", B3 * A, B2 * A, B1 * A, A * B);
	return 0;
}
#endif
