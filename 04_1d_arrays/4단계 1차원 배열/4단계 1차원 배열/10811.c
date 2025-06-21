#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void reverse_arr(int arr[], int i, int j) {
	int start = i;
	int end = j;
	while (start < end) {
		int tmp;
		tmp = arr[start];
		arr[start] = arr[end];
		arr[end] = tmp;
		start++;
		end--;
	}
}

int main() {

	int n, m;
	int arr[101];
	for (int i = 0; i < 101; i++) {
		arr[i] = i;
	}

	scanf("%d %d", &n, &m);
	for (int i = 0; i < m; i++) {
		int i, j;
		scanf("%d %d", &i, &j);
		reverse_arr(arr, i, j);
	}

	for (int i = 1; i <= n; i++) {
		printf("%d ", arr[i]);
	}

	return 0;
}