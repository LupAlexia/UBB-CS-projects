#pragma once
#include "TrenchCoat.h"
#include <string>

class ValidationException: public std::exception { // the exception to be thrown by the validator
private:
	std::string message;
public:
	ValidationException(const std::string& message) : message{ message } {} // constructor
	const char* what() const noexcept override { 
		return this->message.c_str(); } // method to get the error message

};

class TrenchCoatValidator {
public:
	static void validate(const TrenchCoat& trenchCoat);
};