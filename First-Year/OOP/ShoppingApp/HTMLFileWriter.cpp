#include "HTMLFileWriter.h"
using namespace std;

HTMLFileWriter::HTMLFileWriter(const std::string& filename) : filename{ filename } {}

void HTMLFileWriter::writeToFile(const std::vector<TrenchCoat>& trenchCoats)
{
	ofstream file{ filename };

	if (!file.is_open())
	{
		throw std::runtime_error("Could not open file for writing.");
	}

	file << "<!DOCTYPE html><html><body><table border=\"1\">\n";
	file << "<tr><th>Size</th><th>Colour</th><th>Price</th><th>Quantity</th><th>Photograph</th></tr>\n";
	for (const auto& coat : trenchCoats)
	{
		file << "<tr>";
		file << "<td>" << coat.getSize() << "</td>";
		file << "<td>" << coat.getColour() << "</td>";
		file << "<td>" << coat.getPrice() << "</td>";
		file << "<td>" << coat.getQuantity() << "</td>";
		file << "<td><img src=\"" << coat.getPhotograph() << "\" alt=\"Trench Coat\" width=\"100\" height=\"100\"></td>";
		file << "</tr>\n";
	}
	file << "</table></body></html>\n";

	file.close();

}

void HTMLFileWriter::openFile() const
{
	string command = "start \"\" \"" + filename + "\""; // open the file with the default program
	system(command.c_str());
}
