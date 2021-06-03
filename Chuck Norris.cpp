#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

int main()
{
	string message, binary = "", result = "";
	getline(cin, message);

	for (size_t i = 0; i < message.size(); ++i)
		binary += bitset<7>(message.c_str()[i]).to_string();

	int mode = -1;
	for (size_t i = 0; i < binary.size(); ++i)
	{
		result += binary[i] == '0' ? mode == 0 ? "0" : " 00 0" : mode == 1 ? "0" : " 0 0";
		mode = binary[i] == '1';
	}
	cout << result.substr(1) << endl;
}