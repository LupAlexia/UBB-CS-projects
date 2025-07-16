#include "TrenchCoatValidator.h"
#include <vector>
#include <string>
#include <cctype>  
#include <algorithm>
using namespace std;

void TrenchCoatValidator::validate(const TrenchCoat& trenchCoat)
{
	vector<string> sizes = { "XS", "S", "M", "L", "XL" };
	string errors;

	if (trenchCoat.getSize().empty())
		errors += "Size cannot be empty!\n";
	if (find(sizes.begin(), sizes.end(), trenchCoat.getSize()) == sizes.end())
		errors += "Size must be one of the following: XS, S, M, L, XL!\n";

	if (trenchCoat.getColour().empty())
		errors += "Colour cannot be empty!\n";
	
	if (trenchCoat.getPrice() <= 0)
		errors += "Price must be a positive number!\n";
	if (trenchCoat.getQuantity() < 0)
		errors += "Quantity cannot be negative!\n";
	if (trenchCoat.getPhotograph().empty())
		errors += "Photograph cannot be empty!\n";

	if (!errors.empty())
		throw ValidationException(errors);
}
