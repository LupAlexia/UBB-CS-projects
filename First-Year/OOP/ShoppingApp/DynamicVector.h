#pragma once
#include <iostream>

template <typename T>
class DynamicVector {
private:
	T* elements;
	int size;
	int capacity;

	void resize(double factor = 2);
public:
	//constructor
	DynamicVector(int capacity = 10);
	DynamicVector(const DynamicVector& v);
	~DynamicVector();

	DynamicVector& operator=(const DynamicVector& v);//assignment operator overloading

	void add(const T& element);//pass by reference, to avoid unnecessary copies
	void remove(int index);
	void update(int index, const T& element);

	T& operator[](int index) const;//dereference operator overloading - accesing data in the vector
	int getSize() const;
	DynamicVector& getAll();
};

//the implementation
template <typename T>
DynamicVector<T>::DynamicVector(int capacity) {
	this->size = 0;
	this->capacity = capacity;
	this->elements = new T[capacity];
}

template <typename T>
DynamicVector<T>::DynamicVector(const DynamicVector& v) {
	this->size = v.size;
	this->capacity = v.capacity;
	this->elements = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elements[i] = v.elements[i];
}

template <typename T>
DynamicVector<T>::~DynamicVector() {
	delete[] this->elements;
}

template <typename T>
DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector& v) {
	if (this == &v)
		return *this;
	this->size = v.size;
	this->capacity = v.capacity;
	delete[] this->elements;
	this->elements = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elements[i] = v.elements[i];
	return *this; //this - pointer to the current object => *this - the object itself
}

template <typename T>
void DynamicVector<T>::add(const T& element) {
	if (this->size == this->capacity)
		this->resize();
	this->elements[this->size++] = element;
}

template<typename T>
void DynamicVector<T>::remove(int index) {
	//if (index < 0 || index >= this->size)
		//return;
	for (int i = index; i < this->size - 1; i++)
		this->elements[i] = this->elements[i + 1];
	this->size--;
}

template<typename T>
void DynamicVector<T>::update(int index, const T& element) {
	//if (index < 0 || index >= this->size)
		//return;
	this->elements[index] = element;
}

template <typename T>
void DynamicVector<T>::resize(double factor) {
	this->capacity *= factor;

	T* newElements = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		newElements[i] = this->elements[i];
	delete[] this->elements;
	this->elements = newElements;
}

template <typename T>
T& DynamicVector<T>::operator[](int index) const {
	return this->elements[index];
}

template <typename T>
int DynamicVector<T>::getSize() const {
	return this->size;
}

template <typename T>
DynamicVector<T>& DynamicVector<T>::getAll() {
	return *this;
}