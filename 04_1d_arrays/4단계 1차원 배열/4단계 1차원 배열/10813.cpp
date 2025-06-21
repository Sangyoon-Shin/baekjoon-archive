#include <iostream>
#include <vector>

using namespace std;

int main() {

	int n, m, j, k;
	
	cin >> n >> m;

	vector<int> arr(n + 1);

	for (int i = 1; i <= n; i++) {
		arr[i] = i;
	}

	for (int i = 0; i < m; i++) {
		cin >> j >> k;
		int tmp = arr[j];
		arr[j] = arr[k];
		arr[k] = tmp;
	}

	for (int i = 1; i <= n; i++) {
		cout << arr[i] << " ";
	}

	return 0;
}