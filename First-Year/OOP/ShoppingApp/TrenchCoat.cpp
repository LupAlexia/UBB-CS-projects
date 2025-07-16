#include "TrenchCoat.h"
#include <string>
#include <iomanip>
#include <vector>
#include <iostream>
#include <sstream>
#pragma message("Compiling FileRepository.cpp")


using namespace std;

//Constructor
TrenchCoat::TrenchCoat(std::string size, std::string colour, double price, int quantity, std::string photograph)
	: size{ size }, colour{ colour }, price{ price }, quantity{ quantity }, photograph{ photograph } {
}

//Getters

//Returns the size of the trench coat
std::string TrenchCoat::getSize() const { return size; }
//Returns the colour of the trench coat
std::string TrenchCoat::getColour() const { return colour; }
//Returns the price of the trench coat
double TrenchCoat::getPrice() const { return price; }
//Returns the quantity of the trench coat
int TrenchCoat::getQuantity() const { return quantity; }
//Returns the photograph of the trench coat
std::string TrenchCoat::getPhotograph() const { return photograph; }

//Setters

//Sets the price of the trench coat to the given value
void TrenchCoat::setPrice(double newPrice) { price = newPrice; }
//Sets the quantity of the trench coat to the given value
void TrenchCoat::setQuantity(int newQuantity) { quantity = newQuantity; }
//Sets the photograph of the trench coat to the given value
void TrenchCoat::setPhotograph(std::string newPhotograph) { photograph = newPhotograph; }

/* Overloading the equality operator
* Input: trenchCoat - a TrenchCoat object
* Output: true - if the trench coat has the same size and colour as the given trench coat
*/
bool TrenchCoat::operator==(const TrenchCoat& trenchCoat) {
	return size == trenchCoat.size && colour == trenchCoat.colour;
}

std::vector<std::string> tokenize(std::string line, char separator)
{
	std::vector<string> tokens;
	std::string token;
	std::stringstream ss(line); // Create a string stream from the line
	
	while (getline(ss, token, separator)) { // Extract tokens separated by the given character
		tokens.push_back(token); // Add the token to the vector
	}
	return tokens;
}


std::istream& operator>>(std::istream& is, TrenchCoat& tc)
{
	std::string line;
	getline(is, line, '\n');
	vector<string> tokens;
	tokens = tokenize(line, ',');

	if (tokens.size() != 5)
		return is;

	tc.size = tokens[0];
	tc.colour = tokens[1];
	tc.price = std::stod(tokens[2]); // string to double
	tc.quantity = std::stoi(tokens[3]);// string to int
	tc.photograph = tokens[4];
	return is;
}

std::ostream& operator<<(std::ostream& os, const TrenchCoat& tc)
{
	os << std::fixed << std::setprecision(2) << tc.size << "," << tc.colour << "," << tc.price << "," << tc.quantity << "," << tc.photograph;
	return os;
}