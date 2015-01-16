#include <iostream>
#include <fstream>
#include <ctime>
#include <cmath>

using namespace std;

int get_rand(int max)
{
	return rand() % (max+1);
}

int main (int argc, char **argv)
{
	if (argc < 3)
	{
		std::cout << "missing filename and data count" << std::endl;
		return 0;
	}

	int cnt = atoi(argv[2]);
	ofstream file(argv[1]);

	srand(time(nullptr));

	file << "Type,Gender,Style,Color" << std::endl;
	for (int i = 0; i < cnt; i++)
	{
		int color = (get_rand(255) << 16) + (get_rand(255) << 8) + get_rand(255);
		file << get_rand(5) << " " << get_rand(1) << " " << get_rand(2) << " " << color << std::endl;
	}

	return 0;
}
