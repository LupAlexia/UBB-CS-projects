#include <fstream>
#include <string>
#include "FileRepository.h"
#include <algorithm>
#include <iterator>
#include <numeric>

using namespace std;

FileRepository::FileRepository(const std::string& filename): filename {filename}
{}

/* Adds a trench coat to the repository.
* Input: trenchCoat - TrenchCoat object.
* Output: true - if the trench coat was added, false - otherwise.
*/
void FileRepository::add(const TrenchCoat& trenchCoat) {
	vector<TrenchCoat> trenchCoats = readFromFile();
	auto poz = find(trenchCoats.begin(), trenchCoats.end(), trenchCoat);
	if (poz != trenchCoats.end())
		throw DuplicateTrenchCoatException();

	trenchCoats.push_back(trenchCoat);
	writeToFile(trenchCoats);
}

/* Removes a trench coat from the repository, with the given size and colour.
* Input: size - string, colour - string.
* Output: true - if the trench coat was removed, false - otherwise.
*/
void FileRepository::remove(std::string size, std::string colour) {
	TrenchCoat c{ size, colour, 0.0, 0, "" };
	vector<TrenchCoat> trenchCoats = readFromFile();
	auto poz = find(trenchCoats.begin(), trenchCoats.end(), c); // find by unique identifiers(size, colour)

	if (poz == trenchCoats.end())
		throw TrenchCoatNotFoundException();

	trenchCoats.erase(poz);
	writeToFile(trenchCoats);
}

/* Updates a trench coat from the repository, with the given size and colour.
* Input: size - string, colour - string, new_trenchCoat - TrenchCoat object.
* Output: true - if the trench coat was updated, false - otherwise.
*/
void FileRepository::update(std::string size, std::string colour, const TrenchCoat& new_trenchCoat) {
	TrenchCoat c{ size, colour, 0.0, 0, "" };
	vector<TrenchCoat> trenchCoats = readFromFile();
	auto poz = find(trenchCoats.begin(), trenchCoats.end(), c); // find by unique identifiers(size, colour)

	if (poz == trenchCoats.end())
		throw TrenchCoatNotFoundException();
	
	*poz = new_trenchCoat;
	writeToFile(trenchCoats);
}
vector<TrenchCoat> FileRepository::getFilteredBySize(std::string size)
{
	vector<TrenchCoat> trenchCoats = readFromFile();
	if (size.empty()) {
		return trenchCoats;
	}

	vector<TrenchCoat> filteredCoats;
	std::copy_if(trenchCoats.begin(), trenchCoats.end(), std::back_inserter(filteredCoats),
		[&size](const TrenchCoat& tc) {return tc.getSize() == size; });
	//lambda function
	//[&size] - captures size from the outer scope
	// (const TrenchCoat& tc) - parameter
	// {return tc.getSize() == size;} - condition
	return filteredCoats;
}

// Returns all the trench coats from the repository.
vector<TrenchCoat> FileRepository::getAll() {
	auto tcs = readFromFile();
	return tcs;
}

double FileRepository::getTotalPrice() const
{
	vector<TrenchCoat> trenchCoats = readFromFile();
	double totalPrice = std::accumulate(trenchCoats.begin(), trenchCoats.end(), 0.0,
		[](double total, const TrenchCoat& tc) {return total + tc.getPrice(); });
	return totalPrice;
}

std::vector<TrenchCoat> FileRepository::readFromFile() const
{
	TrenchCoat tc;
	vector<TrenchCoat> tcs;

	ifstream fin{ this->filename }; // open file by associating input stream
	while (fin >> tc)
		tcs.push_back(tc);

	return tcs;
}

void FileRepository::writeToFile(const std::vector<TrenchCoat>& tcs) const
{
	ofstream fout{ this->filename };
	for (TrenchCoat tc : tcs)
		fout << tc << '\n';
}
