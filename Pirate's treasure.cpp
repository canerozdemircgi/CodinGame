#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int arrW; cin >> arrW; cin.ignore();
	int arrH; cin >> arrH; cin.ignore();

	int** arr = new int*[arrH];
	for (int i = 0; i < arrH; ++i)
	{
		arr[i] = new int[arrW];
		for (int j = 0; j < arrW; ++j)
			cin >> arr[i][j]; cin.ignore();
	}

	int i, j;
	vector<int> result;
	for (i = 0; i < arrH; ++i)
	{
		for (j = 0; j < arrW; ++j)
		{
			if (arr[i][j] == 0)
			{
				for (int dx = -1; dx <= 1; ++dx)
				{
					int xdx = i + dx;
					for (int dy = -1; dy <= 1; ++dy)
					{
						int ydy = j + dy;
						if (xdx >= 0 && xdx < arrW && ydy >= 0 && ydy < arrH)
							if (!(dx == 0 && dy == 0))
								result.push_back(arr[xdx][ydy]);
					}
				}

				vector<int>::iterator it = std::find(result.begin(), result.end(), 0);
				if (it == result.end())
					goto endgame;
				result.clear();
			}
		}
	}

	endgame:
		cout << j << " " << i << endl;
}