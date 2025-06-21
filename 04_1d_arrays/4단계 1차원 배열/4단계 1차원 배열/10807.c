#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX 100

int main(void) {

	int NA = 0;
	int array[MAX] = { 0, };
	int count = 0;
	int find = 0;

	scanf("%d", &NA);
	for (int i = 0; i < NA; i++) {
		scanf("%d", &array[i]);
	}
	scanf("%d", &find);
	for (int i = 0; i < NA; i++) {
		if (array[i] == find) {
			count++;
		}
	}
	printf("%d", count);

	return 0;
}