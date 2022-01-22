#include <iostream>
#include <vector>
#include <algorithm>

std::pair<std::size_t, std::size_t> two_sum(std::vector<int>& numbers, int target)
{
	std::pair<std::size_t, std::size_t> res;
	std::sort(numbers.begin(), numbers.end());
	std::size_t i = 0;
	std::size_t j = numbers.size() - 1;
	while(i != j)
	{
	
		if ((numbers[i] + numbers[j]) > target)
		{
			j--;
		}
		else if ((numbers[i] + numbers[j]) < target)
		{
			i++;
		}
		else
		{
			res.first = i;
			res.second = j;
			return res;
		}
	}
}

int main()
{
	std::vector<int> v1;
	int tar;		
	int k;
	while (k != 0)
	{	
		std::cin >> k;
		if (k == 0)
			break;
		v1.push_back(k);
	}
	std::cin >> tar;
	std::pair<std::size_t, std::size_t> r;
	r = two_sum(v1, tar);
	std::cout << r.first << " " << r.second;

	return 0;
}