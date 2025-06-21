#include <iostream>
#include <vector>

using namespace std;

int main() {

	int n, m;
	int i, j, k;

	cin >> n >> m;
	vector<int> arr(n + 1);

	for (int l = 0; l < m; l++) {
		cin >> i >> j >> k;
		for (int x = i; x <= j; x++) {
			arr[x] = k;
		}
	}

	for (int x = 1; x <= n; x++) {
		cout << arr[x] << " ";
	}

	return 0;
}