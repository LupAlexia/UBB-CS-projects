#include "Action.h"
#include "Exceptions.h"

ActionAdd::ActionAdd(IRepository& repo, const TrenchCoat& coat) : repo{ repo }, coat{ coat } {}

void ActionAdd::undo() {
    repo.remove(coat.getSize(), coat.getColour());
}

void ActionAdd::redo() {
    repo.add(coat);
}


ActionRemove::ActionRemove(IRepository& repo, const TrenchCoat& coat) : repo{ repo }, coat{ coat } {}

void ActionRemove::undo() {
    repo.add(coat);
}

void ActionRemove::redo() {
    repo.remove(coat.getSize(), coat.getColour());
}

// UndoUpdate
ActionUpdate::ActionUpdate(IRepository& repo, const TrenchCoat& oldCoat, const TrenchCoat& newCoat)
    : repo{ repo }, oldCoat{ oldCoat }, newCoat{ newCoat } {
}

void ActionUpdate::undo() {
    repo.update(oldCoat.getSize(), oldCoat.getColour(), oldCoat);
}

void ActionUpdate::redo() {
    repo.update(newCoat.getSize(), newCoat.getColour(), newCoat);
}
