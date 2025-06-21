#include <iostream>
#include <string>
#include <algorithm>
#include <iterator>

using namespace std;

int main() {

	string s1, s2;

	cin >> s1 >> s2;

	reverse(s1.begin(), s1.end());
	reverse(s2.begin(), s2.end());


	int i1, i2;
	i1 = stoi(s1);
	i2 = stoi(s2);

	int reversesum = i1 + i2;
	
	string result = to_string(reversesum);

	reverse(result.begin(), result.end());

	result.erase(0, result.find_first_not_of('0'));

	cout << result;

	return 0;
}