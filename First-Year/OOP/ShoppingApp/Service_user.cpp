#include "Service_user.h"

UserService::UserService(IRepository& trenchCoatsRepo, IRepository& bagRepo) : trenchCoatsRepo{ trenchCoatsRepo }, bagRepo{ bagRepo } {}

void UserService::setFileWriter(std::unique_ptr<FileWriter> writer)
{
	this->fileWriter = std::move(writer);
}

std::unique_ptr<FileWriter> UserService::getFileWriter()
{
	return std::move(this->fileWriter);
}

void UserService::saveBagToFile()
{
	if (this->fileWriter)
		this->fileWriter->writeToFile(this->bagRepo.getAll());
}

void UserService::openFile()
{
	this->fileWriter->openFile();
}

void UserService::addTrenchCoatToBag(TrenchCoat t)
{
	TrenchCoatValidator::validate(t);
	this->bagRepo.add(t);
	saveBagToFile();
}

std::vector<TrenchCoat> UserService::getTrenchCoatsWithSize(std::string size) const
{
	if (size.empty())
		return this->trenchCoatsRepo.getAll();
	else
		return this->trenchCoatsRepo.getFilteredBySize(size);
}

std::vector<TrenchCoat> UserService::getBag() const
{
	return this->bagRepo.getAll();
}

double UserService::getBagPrice() const
{
	return this->bagRepo.getTotalPrice();
}
