#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	while (true)
	{
		int index = -1;
		int highest = -1;
		for (int i = 0; i < 8; i++)
		{
			int mountainH;
			cin >> mountainH; cin.ignore();
			if (highest < mountainH)
			{
				highest = mountainH;
				index = i;
			}
		}

		cout << index << endl;
	}
}