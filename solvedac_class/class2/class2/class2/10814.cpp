#include <iostream>
#include <string>
#include <cstdlib>
#include <algorithm>

using namespace std;

class User {
public:
	int age;
	string name;
};

bool compare(const User& a, const User& b) {
	return a.age < b.age;
}

int main() {

	int n;
	cin >> n;

	User *users = new User[n];

	for (int i = 0; i < n; i++) {
		int myage;
		string myname;
		cin >> myage >> myname;
		
		users[i].age = myage;
		users[i].name = myname;
	}

	stable_sort(users, users + n, compare);

	for (int i = 0; i < n; i++) {
		cout << users[i].age << " " << users[i].name << endl;
	}

	delete[] users;

	return 0;
}