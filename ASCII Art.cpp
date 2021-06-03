#include <iostream>
#include <string>

using namespace std;

int main()
{
	int width, height;
	cin >> width >> height; cin.ignore();

	string text;
	getline(cin, text);
	int textSize = text.size();

	string letters = "abcdefghijklmnopqrstuvwxyz";
	int lettersSize = letters.size();

	string alphabet[height][(lettersSize + 1) * width];
	for (int i = 0; i < height; ++i)
	{
		string line;
		getline(cin, line);

		for (int j = 0; j < lettersSize + 1; ++j)
			alphabet[i][j] = line.substr(j * width, width);

		for (int j = 0; j < textSize; ++j)
		{
			int pos = letters.find(tolower(text[j]));
			if (pos == string::npos)
				pos = lettersSize;
			cout << alphabet[i][pos];
		}
		cout << endl;
	}
}