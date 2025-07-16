#pragma once
#include "Repository.h"
#include "TrenchCoatValidator.h"
#include "FileRepository.h"
#include "Action.h"
#include <stack>
#include <memory>

class Service {
private:
	IRepository& repo;
	std::stack<std::unique_ptr<Action>> undoStack; // use unique pointers because of polimorphism of action classes
	std::stack<std::unique_ptr<Action>> redoStack;
public:
	Service(IRepository& repo);

	void addTrenchCoat(const std::string& size, const std::string& colour, double price, int quantity, const std::string& photograph);
	void removeTrenchCoat(const std::string& size, const std::string& colour);
	void updateTrenchCoat(const std::string& size, const std::string& colour, double price, int quantity, const std::string& photograph);

	std::vector<TrenchCoat> getAllTrenchCoats() const;
	void initializeRepo();

	void undo();
	void redo();
};