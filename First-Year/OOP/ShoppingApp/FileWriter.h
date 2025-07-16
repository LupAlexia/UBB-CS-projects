#pragma once
#include "TrenchCoat.h"
#include <vector>

class FileWriter {
public:
	virtual void writeToFile(const std::vector<TrenchCoat>& trenchCoats) = 0;
	virtual void openFile() const = 0;
	virtual ~FileWriter() = default;
};