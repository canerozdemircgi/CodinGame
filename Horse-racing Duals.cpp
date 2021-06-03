#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int N;
	cin >> N; cin.ignore();

	int Pis[N];
	for (int i = 0; i < N; ++i)
		cin >> Pis[i]; cin.ignore();

	sort(Pis, Pis + N);
	int answer = 2147483647;
	int temp;
	for (int i = 0; i < N - 1; ++i)
	{
			temp = abs(Pis[i] - Pis[i + 1]);
			if (answer > temp)
				answer = temp;
	}

	cout << answer << endl;
}