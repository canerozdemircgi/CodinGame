#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int surfaceN;
	cin >> surfaceN; cin.ignore();
	for (int i = 0; i < surfaceN; i++)
	{
		int landX;
		int landY;
		cin >> landX >> landY; cin.ignore();
	}

	while (true)
	{
		int X;
		int Y;
		int hSpeed;
		int vSpeed;
		int fuel;
		int rotate;
		int power;
		cin >> X >> Y >> hSpeed >> vSpeed >> fuel >> rotate >> power; cin.ignore();

		vSpeed = abs(vSpeed);
		if (vSpeed >= 32)
			cout << "0 4" << endl;
		else if (vSpeed >= 16)
			cout << "0 3" << endl;
		else if (vSpeed >= 8)
			cout << "0 2" << endl;
		else
			cout << "0 1" << endl;
	}
}