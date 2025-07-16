#pragma once
#include "TrenchCoat.h"
#include "Exceptions.h"
#include <vector>

//Pure abstract class/Interface
class IRepository {
public:
	//only pure virtual functions
	virtual void add(const TrenchCoat& trenchCoat) = 0;
	virtual void remove(std::string size, std::string colour) = 0;
	virtual void update(std::string size, std::string colour, const TrenchCoat& new_trenchCoat) = 0;

	virtual std::vector<TrenchCoat> getFilteredBySize(std::string size) = 0;
	virtual std::vector<TrenchCoat> getAll() = 0;

	virtual double getTotalPrice() const = 0;

	virtual ~IRepository() = default;
};