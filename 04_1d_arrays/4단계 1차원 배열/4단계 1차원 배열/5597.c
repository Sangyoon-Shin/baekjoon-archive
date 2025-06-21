#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int n = 0;
	int list[31] = { 0, };	// 체크리스트 모두 0으로 초기화

	int xlist[2] = { 0, }; // 제출 안한 애들 번호 저장할 배열

	int idx = 1; // list의 인덱스 나타낼 값. 번호는 1번부터니까 초기값 1
	int xidx = 0; // list에서 값이 0인 인덱스를 저장하기 위한 배열의 인덱스 나타내기 위함.

	for (int i = 0; i < 28; i++) { 
		scanf("%d", &n);	
		list[n] = 1;	
	}

	do {
		if (list[idx] == 0) { // 제출명단에서 값이 0인 인덱스를 찾기
			xlist[xidx] = idx;
			xidx++;
		}
		idx++;
	} while (idx != 31);

	printf("%d\n%d", xlist[0], xlist[1]);
	

	return 0;
}