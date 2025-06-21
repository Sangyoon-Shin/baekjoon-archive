#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int max_index = 0;
	int array[9] = { 0, };
	int max = 0;

	int n;
	for (int i = 0; i < 9; i++) {
		scanf("%d", &n);
		if (n > max) {
			array[i] = n;
			max_index = i;
			max = array[i];
		}
		else {
			array[i] = n;
		}
	}

	printf("%d\n", max);
	printf("%d", max_index+1);

	return 0;
}
