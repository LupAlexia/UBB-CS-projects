#pragma once
#include "TrenchCoat.h"
#include <vector>
#include "IRepository.h"

class FileRepository : public IRepository {
private:
	std::string filename;
public:
	FileRepository(const std::string& filename);
	void add(const TrenchCoat& trenchCoat) override;
	void remove(std::string size, std::string colour) override;
	void update(std::string size, std::string colour, const TrenchCoat& new_trenchCoat) override;

	std::vector<TrenchCoat> getFilteredBySize(std::string size) override;
	std::vector<TrenchCoat> getAll() override;

	double getTotalPrice() const override;
private:
	std::vector<TrenchCoat> readFromFile() const;
	void writeToFile(const std::vector<TrenchCoat>& tcs) const;
};