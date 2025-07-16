#include <iostream>
#include <string>
#include "Repository.h"
#include <algorithm>
#include <iterator>
#include <numeric>

using namespace std;

/* Adds a trench coat to the repository.
* Input: trenchCoat - TrenchCoat object.
* Output: true - if the trench coat was added, false - otherwise.
*/
void Repository::add(const TrenchCoat& trenchCoat) {
	auto poz = find(this->trenchCoats.begin(), this->trenchCoats.end(), trenchCoat);
	if (poz != this->trenchCoats.end())
		throw DuplicateTrenchCoatException();
	
	this->trenchCoats.push_back(trenchCoat);
}

/* Removes a trench coat from the repository, with the given size and colour.
* Input: size - string, colour - string.
* Output: true - if the trench coat was removed, false - otherwise.
*/
void Repository::remove(std::string size, std::string colour) {
	TrenchCoat c{ size, colour, 0.0, 0, "" };
	auto poz = find(this->trenchCoats.begin(), this->trenchCoats.end(), c); // find by unique identifiers(size, colour)
	
	if (poz == this->trenchCoats.end())
		throw TrenchCoatNotFoundException();
	this->trenchCoats.erase(poz);
}

/* Updates a trench coat from the repository, with the given size and colour.
* Input: size - string, colour - string, new_trenchCoat - TrenchCoat object.
* Output: true - if the trench coat was updated, false - otherwise.
*/
void Repository::update(std::string size, std::string colour, const TrenchCoat& new_trenchCoat) {
	TrenchCoat c{ size, colour, 0.0, 0, "" };
	auto poz = find(this->trenchCoats.begin(), this->trenchCoats.end(), c); // find by unique identifiers(size, colour)

	if (poz == this->trenchCoats.end())
		throw TrenchCoatNotFoundException();

	*poz = new_trenchCoat;
}
vector<TrenchCoat> Repository::getFilteredBySize(std::string size)
{
	if (size.empty()) {
		return this->trenchCoats;
	}

	vector<TrenchCoat> filteredCoats;
	std::copy_if(this->trenchCoats.begin(), this->trenchCoats.end(), std::back_inserter(filteredCoats),
		[&size](const TrenchCoat& tc) {return tc.getSize() == size;});
	//lambda function
	//[&size] - captures size from the outer scope
	// (const TrenchCoat& tc) - parameter
	// {return tc.getSize() == size;} - condition
	return filteredCoats;
}

// Returns all the trench coats from the repository.
vector<TrenchCoat> Repository::getAll() {
	return this->trenchCoats;
}

double Repository::getTotalPrice() const
{
	double totalPrice = std::accumulate(trenchCoats.begin(), trenchCoats.end(), 0.0,
		[](double total, const TrenchCoat& tc) {return total + tc.getPrice(); });
	return totalPrice;
}
