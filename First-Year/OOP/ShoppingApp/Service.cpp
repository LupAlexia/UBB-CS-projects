#include "Service.h"
#include <iostream>

//Constructor 
Service::Service(IRepository& repo) : repo{ repo } {}

/*
* Adds a trench coat to the repository, by calling the add function from the repository
* Input: size, colour, price, quantity, photograph - strings
* Output: true - if the trench coat was added successfully
*/
void Service::addTrenchCoat(const std::string& size, const std::string& colour, double price, int quantity, const std::string& photograph) {
    TrenchCoat trenchCoat{ size, colour, price, quantity, photograph };
    TrenchCoatValidator::validate(trenchCoat);

    this->repo.add(trenchCoat);
    undoStack.push(std::make_unique<ActionAdd>(repo, trenchCoat));
    redoStack = {};
}

/*
* Removes a trench coat from the repository, based on the size and colour, by calling the remove function from the repository
* Input: size, colour - strings
* Output: true - if the trench coat was removed successfully
*/
void Service::removeTrenchCoat(const std::string& size, const std::string& colour) {
	TrenchCoat c{ size, colour, 1, 1, "string" };
    TrenchCoatValidator::validate(c);

    auto coats = repo.getAll();
    auto it = std::find(coats.begin(), coats.end(), TrenchCoat(size, colour, 0.0, 0, ""));
    if (it == coats.end())
        throw TrenchCoatNotFoundException();

    TrenchCoat deletedCoat = *it;

    this->repo.remove(size, colour);
    undoStack.push(std::make_unique<ActionRemove>(repo, deletedCoat));
    redoStack = {};
}

/*
* Updates a trench coat from the repository, based on the size and colour, by calling the update function from the repository
* Input: size, colour, price, quantity, photograph - strings
* Output: true - if the trench coat was updated successfully
*/
void Service::updateTrenchCoat(const std::string& size, const std::string& colour, double price, int quantity, const std::string& photograph) {
    TrenchCoat new_trenchCoat{ size, colour, price, quantity, photograph };
	TrenchCoatValidator::validate(new_trenchCoat);

    auto coats = repo.getAll();
    auto it = std::find(coats.begin(), coats.end(), TrenchCoat(size, colour, 0.0, 0, ""));
    if (it == coats.end())
        throw TrenchCoatNotFoundException();

    TrenchCoat oldCoat = *it;

    this->repo.update(size, colour, new_trenchCoat);
    undoStack.push(std::make_unique<ActionUpdate>(repo, oldCoat, new_trenchCoat));
    redoStack = {};
}

/*
* Returns all the trench coats from the repository
* Output: a dynamic vector containing all the trench coats
*/
std::vector<TrenchCoat> Service::getAllTrenchCoats() const {
    return this->repo.getAll();
}
void Service::initializeRepo()
{
    this->addTrenchCoat("M", "Black", 120.5, 10, "https://www.zalando.ro/lauren-ralph-lauren-lined-coat-trenci-navy-l4221u0by-k11.html");
    this->addTrenchCoat("L", "Purple", 150.0, 5, "https://us.maxmara.com/p-9021105406016-utrench-clay");
    this->addTrenchCoat("S", "Red", 130.0, 9, "https://www.zalando.ro/lauren-ralph-lauren-lined-trenci-birch-tan-l4221u0c7-b11.html");
    this->addTrenchCoat("XS", "Beige", 230.0, 7, "https://au.maxmara.com/p-5071015106001-vivetta-beige");
    this->addTrenchCoat("L", "Pink", 180.0, 95, "https://us.shein.com/Women-Trench-Coats-c-3050.html");
    this->addTrenchCoat("S", "White", 115.5, 8, "https://www.zalando.ro/calvin-klein-trench-coat-trenci-white-pepper-6ca21u07o-b11.html");
    this->addTrenchCoat("XL", "Khaki", 80.0, 2, "https://www.zalando.ro/polo-ralph-lauren-hooded-trench-coat-trenci-classic-khaki-po223r001-n11.html");
    this->addTrenchCoat("S", "Brown", 92.0, 34, "https://us.shein.com/Men-Trench-Coats-c-3136.html");
    this->addTrenchCoat("M", "White", 110.0, 7, "https://us.maxmara.com/v/trench-coats-female");
    this->addTrenchCoat("L", "Yellow", 128.0, 6, "https://us.shein.com/style/Trench-Outerwear-sc-00105085.html");
}

void Service::undo() {
    if (undoStack.empty())
        throw std::runtime_error("No more undo operations!");
    auto action = std::move(undoStack.top());
    undoStack.pop();
    action->undo();
    redoStack.push(std::move(action));
}

void Service::redo() {
    if (redoStack.empty())
        throw std::runtime_error("No more redo operations!");
    auto action = std::move(redoStack.top());
    redoStack.pop();
    action->redo();
    undoStack.push(std::move(action));
}
