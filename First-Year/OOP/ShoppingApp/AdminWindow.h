#pragma once
#include <QWidget>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QTableWidget>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include "Service.h"
#include "TrenchCoatValidator.h"
#include "Exceptions.h"

class AdminWindow : public QWidget{
	Q_OBJECT
public:
	AdminWindow(Service& service, QWidget* parent = nullptr);
private slots:
	void addTrenchCoat();
	void deleteTrenchCoat();
	void updateTrenchCoat();
	void populateTable();
	void undoAction();
	void redoAction();
private:
	QTableWidget* table;
	QLineEdit * sizeInput, * colorInput, * priceInput, * qtyInput, * photoInput;
	QLabel * sizeLabel, * colorLabel, * priceLabel, * qtyLabel, * photoLabel;
	QPushButton* addButton, * delButton, * updateButton;
	QPushButton* undoButton;
	QPushButton* redoButton;

	Service& service;
	void initUI();
};