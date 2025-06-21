#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX 100

int fibo(int n, int* arr) {

	static int value[MAX];
	if (n < 2) {
		arr[n]++;
		return n;
	}
	if (value[n] > 0) {
		return value[n];
	}
	else {
		return value[n] = fibo(n-1, arr) + fibo(n-2, arr);
	}

}

int main() {

	int n;
	int num;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int arr[2] = { 0, };
		scanf("%d", &num);
		fibo(num, arr);
		printf("%d %d\n", arr[0], arr[1]);
	}

	return 0;
}