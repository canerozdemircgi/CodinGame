#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int lightX;
	int lightY;
	int initialTX;
	int initialTY;
	cin >> lightX >> lightY >> initialTX >> initialTY; cin.ignore();

	int x = lightX - initialTX;
	int y = lightY - initialTY;

	while (true)
	{
		int remainingTurns;
		cin >> remainingTurns; cin.ignore();

		if (x > 0 && y > 0)
		{
			--x; --y;
			cout << "SE" << endl;
		}
		else if (x < 0 && y < 0)
		{
			++x; ++y;
			cout << "NW" << endl;
		}
		else if (x > 0 && y < 0)
		{
			--x; ++y;
			cout << "NE" << endl;
		}
		else if (x < 0 && y > 0)
		{
			++x; --y;
			cout << "SW" << endl;
		}
		else if (y > 0)
		{
			--y;
			cout << "S" << endl;
		}
		else if (y < 0)
		{
			++y;
			cout << "N" << endl;
		}
		else if (x > 0)
		{
			--x;
			cout << "E" << endl;
		}
		else if (x < 0)
		{
			++x;
			cout << "W" << endl;
		}
	}
}