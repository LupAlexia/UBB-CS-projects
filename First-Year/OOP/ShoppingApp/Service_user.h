#pragma once
#include "Repository.h"
#include "FileRepository.h"
#include "TrenchCoatValidator.h"
#include "CSVFileWriter.h"
#include "HTMLFileWriter.h"
#include <memory>

class UserService {
private:
	IRepository& trenchCoatsRepo;
	IRepository& bagRepo;
	std::unique_ptr<FileWriter> fileWriter;

public:
	UserService(IRepository& trenchCoatsRepo, IRepository& bagRepo);
	void setFileWriter(std::unique_ptr<FileWriter> writer);
	std::unique_ptr<FileWriter> getFileWriter();

	void saveBagToFile();
	void openFile();

	void addTrenchCoatToBag(TrenchCoat t);

	std::vector<TrenchCoat> getTrenchCoatsWithSize(std::string size) const;
	std::vector<TrenchCoat> getBag() const;
	double getBagPrice() const;
};