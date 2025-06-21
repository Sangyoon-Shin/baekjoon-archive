#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void) {

	int n;
	double max = 0;
	double score[1000]; // 실제 점수 저장할 배열
	double new_score[1000];	// 변경한 점수 저장할 배열
	double sum = 0; // 변경한 점수들의 합 저장할 변수
	double new_avg = 0;	// 변경한 점수들의 평균 나타낼 변수

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%lf", &score[i]);	
		if (score[i] >= max) {	// 실제 점수 중에서 최대값 구하기
			max = score[i];
		}
	}

	for (int i = 0; i < n; i++) {
		new_score[i] = score[i] * 1 / max * 100; // 문제에 나타난 공식 적용시킨 점수를 새로운 배열에 저장
		sum = sum + new_score[i];	// 새로운 배열의 모든 값들의 합
	}

	new_avg = sum / n; // 변경한 점수들 평균 구하기

	printf("%lf", new_avg);

	return 0;
}