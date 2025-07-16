#pragma once
#include <exception>
#include <string>

using namespace std;

class RepositoryException : public exception {
private:
	string message;
public:
	RepositoryException(const string& message) : message{ message } {} // constructor
	const char* what() const noexcept override {
		return this->message.c_str();
	}
};

class DuplicateTrenchCoatException : public RepositoryException {
public:
	DuplicateTrenchCoatException() : RepositoryException{ "Trench coat already exists!" } {} // constructor 
};

class TrenchCoatNotFoundException : public RepositoryException {
public:
	TrenchCoatNotFoundException() : RepositoryException{ "Trench coat not found!" } {}
};
