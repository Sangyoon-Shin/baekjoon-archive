#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

    int T, N, D;
    int v, f, c;

    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        scanf("%d %d", &N, &D);
        int count = 0;
        for (int j = 0; j < N; j++) {
            scanf("%d %d %d", &v, &f, &c);
            if (D <= (double)v * ((double)f / (double)c)) {
                count++;
            }
        }
        printf("%d\n", count); 
    }

    return 0;
}
