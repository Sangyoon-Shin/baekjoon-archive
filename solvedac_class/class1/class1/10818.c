#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int n;
int value[1000001];
int max = -1000001;
int min = 1000001;

int main(void) {

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &value[i]);
		if (value[i] >= max) {
			max = value[i];
		}
		if (value[i] <= min) {
			min = value[i];
		}
	}

	printf("%d %d", min, max);

	return 0;
}

#if 0
int main(void) {

	int n;
	int value[1000001];
	int max = -1000001;
	int min = 1000001;

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &value[i]);
		if (value[i] >= max) {
			max = value[i];
		}
		if (value[i] <= min) {
			min = value[i];
		}
	}

	printf("%d %d", min, max);

	return 0;
}
#endif