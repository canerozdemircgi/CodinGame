#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main()
{
	int n; cin >> n; cin.ignore();

	int result = INT_MIN + 1;
	for (int i = 0; i < n; ++i)
	{
		int val; cin >> val; cin.ignore();
		if (abs(val) < abs(result))
			result = val;
		else if (abs(val) == abs(result))
		{
			if (val > 0)
				result = val;
		}
	}
	if (result == INT_MIN + 1)
		result = 0;

	cout << result << endl;
}