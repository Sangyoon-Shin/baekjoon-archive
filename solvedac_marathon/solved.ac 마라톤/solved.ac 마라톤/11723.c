#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

void add(int arr[], int value) {
	arr[value] = value;
}

void my_remove(int arr[], int value) {
	arr[value] = 0;
}

void check(int arr[], int value) {
	if (arr[value] != 0) {
		printf("1\n");
	}
	else {
		printf("0\n");
	}
}

void toggle(int arr[], int value) {
	if (arr[value] == value) {
		arr[value] = 0;
	}
	else {
		arr[value] = value;
	}
}

void all(int arr[]) {
	for (int i = 1; i < 21; i++) {
		arr[i] = i;
	}
}

void empty(int arr[]) {
	for (int i = 1; i < 21; i++) {
		arr[i] = 0;
	}
}

int main() {

	int n;
	int value;
	int arr[21] = { 0, };
	char str[10];

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%s %d", str, &value);
		if (strcmp(str, "add") == 0) {
			add(arr, value);
		}
		else if (strcmp(str, "remove") == 0) {
			my_remove(arr, value);
		}
		else if (strcmp(str, "check") == 0) {
			check(arr, value);
		}	
		else if (strcmp(str, "toggle") == 0) {
			toggle(arr, value);
		}
		else if (strcmp(str, "all") == 0) {
			all(arr);
		}
		else if (strcmp(str, "empty") == 0) {
			empty(arr);
		}
	}

	return 0;
}