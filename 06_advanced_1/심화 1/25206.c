#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	double sum = 0.0;
	double point_sum = 0.0;

	for (int i = 0; i < 20; i++) {
		char subject[51];
		double point = 0;
		char grade[3];
		scanf(" %s %lf %s", subject, &point, grade);
		if (strcmp(grade, "P") == 0) {
			continue;
		}
		else if (strcmp(grade, "F") == 0) {
			point_sum = point_sum + point;
		}
		else if (strcmp(grade, "A+")== 0) {
			sum = sum + (4.5 * point);
			point_sum = point_sum + point;
		}
		else if (strcmp(grade, "A0") == 0) {
			sum = sum + (4.0 * point);
			point_sum = point_sum + point;
		}
		else if (strcmp(grade, "B+") == 0) {
			sum = sum + (3.5 * point);
			point_sum = point_sum + point;
		}
		else if (strcmp(grade, "B0") == 0) {
			sum = sum + (3.0 * point);
			point_sum = point_sum + point;
		}
		else if (strcmp(grade, "C+") == 0) {
			sum = sum + (2.5 * point);
			point_sum = point_sum + point;
		}
		else if (strcmp(grade, "C0") == 0) {
			sum = sum + (2.0 * point);
			point_sum = point_sum + point;
		}
		else if (strcmp(grade, "D+") == 0) {
			sum = sum + (1.5 * point);
			point_sum = point_sum + point;
		}
		else if (strcmp(grade, "D0") == 0) {
			sum = sum + (1.0 * point);
			point_sum = point_sum + point;
		}
	}
	double avg = sum / point_sum;

	printf("%lf", avg);


	return 0;
}