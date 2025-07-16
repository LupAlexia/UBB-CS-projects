#pragma once
#include <QWidget>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QPixmap>
#include <QDesktopServices>
#include <QTableView>
#include <QUrl>
#include "Service_user.h"
#include "ShoppingBagModel.h"

class UserWindow : public QWidget{
	Q_OBJECT
public:
	UserWindow(UserService& user_service, QWidget* parent = nullptr);

private slots:
	void filterTrenchCoats();
	void displayNextTrenchCoat();
	void addToBasket();
	void displayShoppingBasket();
	void openShoppingBasketFile();
	void showShoppingBagTable();

private:
	void initUI();

	int currentIndex = 0; // Index of the currently displayed trench coat
	std::vector<TrenchCoat> filteredCoats;
	double totalPrice = 0;

	void updateDisplay();

    QLineEdit* sizeInput;
    QLabel* coatDetails;
    QLabel* coatImage, *instructions;
    QPushButton* filterBtn, * nextBtn, * addBtn, * basketBtn, * openFileBtn;
	QPushButton* showBagTableButton;

	QTableView* bagTableView;
	ShoppingBagModel* bagModel;
    UserService& user_service;
};