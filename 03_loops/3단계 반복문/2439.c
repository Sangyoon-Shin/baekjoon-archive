#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    for (int i = 1; i <= N; i++) {
        // 공백 출력
        for (int j = 1; j <= N - i; j++) {
            printf(" ");
        }
        // 별 출력
        for (int j = 1; j <= i; j++) {
            printf("*");
        }

        printf("\n");
    }
    return 0;
}
