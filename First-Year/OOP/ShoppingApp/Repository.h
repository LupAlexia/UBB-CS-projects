#pragma once
#include "TrenchCoat.h"
#include <vector>
#include "IRepository.h"

class Repository: public IRepository {
private:
	std::vector<TrenchCoat> trenchCoats;
public:
	void add(const TrenchCoat& trenchCoat) override;
	void remove(std::string size, std::string colour) override;
	void update(std::string size, std::string colour, const TrenchCoat& new_trenchCoat) override;

	std::vector<TrenchCoat> getFilteredBySize(std::string size) override;
	std::vector<TrenchCoat> getAll() override;

	double getTotalPrice() const override;
};