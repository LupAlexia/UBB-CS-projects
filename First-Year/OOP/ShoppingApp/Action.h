#pragma once
#include "TrenchCoat.h"
#include "IRepository.h"

class Action {
public:
    virtual void undo() = 0;
    virtual void redo() = 0;
    virtual ~Action() = default;
};

class ActionAdd : public Action {
private:
    IRepository& repo;
    TrenchCoat coat;
public:
    ActionAdd(IRepository& repo, const TrenchCoat& coat);
    void undo() override;
    void redo() override;
};

class ActionRemove : public Action {
private:
    IRepository& repo;
    TrenchCoat coat;
public:
    ActionRemove(IRepository& repo, const TrenchCoat& coat);
    void undo() override;
    void redo() override;
};

class ActionUpdate : public Action {
private:
    IRepository& repo;
    TrenchCoat oldCoat;
    TrenchCoat newCoat;
public:
    ActionUpdate(IRepository& repo, const TrenchCoat& oldCoat, const TrenchCoat& newCoat);
    void undo() override;
    void redo() override;
};

