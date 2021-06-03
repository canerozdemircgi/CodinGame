#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int N;
string *operation, *arg1, *arg2;
char *state;
int *result;

int recurse(int i)
{
	if (state[i] == '1')
		return result[i];

	int x;
	if (arg1[i][0] == '$')
		x = recurse(std::stoi(arg1[i].substr(1)));
	else
		x = std::stoi(arg1[i]);

	if (operation[i] == "VALUE")
	{
		state[i] = '1';
		result[i] = x;
		return result[i];
	}

	int y;
	if (arg2[i][0] == '$')
		y = recurse(std::stoi(arg2[i].substr(1)));
	else
		y = std::stoi(arg2[i]);

	if (operation[i] == "ADD")
	{
		state[i] = '1';
		result[i] = x + y;
		return result[i];
	}
	if (operation[i] == "SUB")
	{
		state[i] = '1';
		result[i] = x - y;
		return result[i];
	}
	if (operation[i] == "MULT")
	{
		state[i] = '1';
		result[i] = x * y;
		return result[i];
	}
}

int main()
{
	cin >> N; cin.ignore();

	operation = new string[N];
	arg1 = new string[N];
	arg2 = new string[N];

	state = new char[N];
	result = new int[N];

	for (int i = 0; i < N; i++)
	{
		cin >> operation[i] >> arg1[i] >> arg2[i]; cin.ignore();

		state[i] = '0';
		result[i] = 0;
	}

	for (int i = 0; i < N; i++)
	{
		cout << recurse(i) << endl;
	}
}