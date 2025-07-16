#pragma once
#include "FileWriter.h"
#include <fstream>
#include <string>

class CSVFileWriter : public FileWriter {
private:
	std::string filename;

public:
	CSVFileWriter(const std::string& filename);
	void writeToFile(const std::vector<TrenchCoat>& trenchCoats) override;
	void openFile() const override;
};