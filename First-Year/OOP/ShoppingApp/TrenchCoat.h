#pragma once
#include <string>

class TrenchCoat {
private:
	std::string size;
	std::string colour;
	double price;
	int quantity;
	std::string photograph; //URL

public:
	TrenchCoat(std::string size = "", std::string colour = "", double price = 0, int quantity = 0, std::string photograph = "");
	std::string getSize() const;
	std::string getColour() const;
	double getPrice() const;
	int getQuantity() const;
	std::string getPhotograph() const;

	void setPrice(double newPrice);
	void setQuantity(int newQuantity);
	void setPhotograph(std::string newPhotograph);

	bool operator==(const TrenchCoat& trenchCoat);
	friend std::istream& operator>>(std::istream& is, TrenchCoat& tc);
	friend std::ostream& operator<<(std::ostream& os, const TrenchCoat& tc);

}; 
