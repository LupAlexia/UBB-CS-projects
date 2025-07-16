#include "CSVFileWriter.h"
using namespace std;

CSVFileWriter::CSVFileWriter(const std::string& filename) : filename{ filename }  {}

void CSVFileWriter::writeToFile(const std::vector<TrenchCoat>& trenchCoats)
{
	ofstream file{ filename };

	if (!file.is_open())
	{
		throw std::runtime_error("Could not open file for writing.");
	}

	for (const auto& coat : trenchCoats)
		file << coat.getSize() << "," << coat.getColour() << "," << coat.getPrice() << ","<< coat.getQuantity() << ","<< coat.getPhotograph() << "\n";
	
	file.close();

}

void CSVFileWriter::openFile() const
{
	string command = "start \"\" \"" + filename + "\""; // open the file with the default program
	system(command.c_str());
}
