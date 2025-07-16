#include "UserWindow.h"
#include <QMessageBox>

UserWindow::UserWindow(UserService& user_service,QWidget* parent) : QWidget(parent), user_service(user_service)
{
	this->setWindowTitle("User Panel");
    this->resize(800, 600);
	initUI();
}
void UserWindow::filterTrenchCoats()
{
    std::string size = sizeInput->text().toStdString();
 
    if (size.empty())
		filteredCoats = user_service.getTrenchCoatsWithSize("");
	else
        filteredCoats = user_service.getTrenchCoatsWithSize(size);
	currentIndex = 0;

	if (filteredCoats.empty()) {
		coatDetails->setText("No trench coats found.");
		nextBtn->setEnabled(false);
		addBtn->setEnabled(false);
		return;
	}

	// Display the first trench coat
	updateDisplay();

	// Enable the Next and Add to Basket buttons
	nextBtn->setEnabled(true);
	addBtn->setEnabled(true);

	// Clear the size input
	sizeInput->clear();
}

void UserWindow::displayNextTrenchCoat() // go to next trench coat
{
	if (filteredCoats.empty()) return;

	currentIndex = (currentIndex + 1) % filteredCoats.size();
	updateDisplay();
}

void UserWindow::updateDisplay() // Display the current trench coat details
{
    const TrenchCoat& coat = filteredCoats[currentIndex];
    coatDetails->setText(QString("Size: %1\nColor: %2\nPrice: %3\nQuantity: %4")
        .arg(QString::fromStdString(coat.getSize()))
        .arg(QString::fromStdString(coat.getColour()))
        .arg(coat.getPrice())
        .arg(coat.getQuantity()));

    std::string command = "start \"\" \"" + coat.getPhotograph() + "\"";
    system(command.c_str());
}

void UserWindow::addToBasket() //add current coat to basket and update total price
{
    if (filteredCoats.empty()) return;

    const TrenchCoat& coat = filteredCoats[currentIndex];

    try {
		user_service.addTrenchCoatToBag(coat);
	}
    catch (const DuplicateTrenchCoatException& e) {
        QMessageBox::critical(this, "Error", e.what());
        return;
    }
    totalPrice += coat.getPrice();

    // Update the display to show the new total price
    coatDetails->setText(QString("Total Price: %1").arg(totalPrice));
    QMessageBox::information(this, "Success", "Trench coat added to basket!");
}

void UserWindow::displayShoppingBasket()
{
	std::vector <TrenchCoat> basket = user_service.getBag();
    if (filteredCoats.empty()) {
        coatDetails->setText("No trench coats found.");
        return;
    }
	QString basketDetails;
	for (const auto& coat : basket) {
		basketDetails += QString("Size: %1 | Color: %2 | Price: %3 | Quantity: %4\n")
			.arg(QString::fromStdString(coat.getSize()))
			.arg(QString::fromStdString(coat.getColour()))
			.arg(coat.getPrice())
			.arg(coat.getQuantity());
	}
	basketDetails += QString("\n Total Price: %1").arg(user_service.getBagPrice());
	coatDetails->setText(basketDetails);
}

void UserWindow::openShoppingBasketFile()
{
	user_service.openFile();
}

void UserWindow::showShoppingBagTable()
{
	if (bagTableView->isVisible()) {
		bagTableView->hide();
		showBagTableButton->setText("Show Shopping Bag Table");
	}
	else {
		bagModel->update(); // Refresh the model to ensure it has the latest data
		bagTableView->show();
		showBagTableButton->setText("Hide Shopping Bag Table");
	}
}

void UserWindow::initUI() {
    auto* layout = new QVBoxLayout();

    instructions = new QLabel("Choose an option:");
    layout->addWidget(instructions);

    // Option 1: Search by size
    auto* searchLayout = new QHBoxLayout();
    sizeInput = new QLineEdit();
    sizeInput->setPlaceholderText("Enter size (or leave empty)");
    filterBtn = new QPushButton("Search");
    searchLayout->addWidget(sizeInput);
    searchLayout->addWidget(filterBtn);
    layout->addLayout(searchLayout);

    // Trench coat display section
    coatDetails = new QLabel("Trench coat details will appear here");
	coatDetails->setWordWrap(true); // Enable word wrapping 

    layout->addWidget(coatDetails);

    // Next and Add to Basket
    auto* navLayout = new QHBoxLayout();
    nextBtn = new QPushButton("Next");
    addBtn = new QPushButton("Add to Basket");
    navLayout->addWidget(nextBtn);
    navLayout->addWidget(addBtn);
    layout->addLayout(navLayout);

    // Option 2 and 3
    basketBtn = new QPushButton("Display Shopping Basket");
    openFileBtn = new QPushButton("Open Shopping Basket File");
	showBagTableButton = new QPushButton("Show Shopping Bag Table");

    layout->addWidget(basketBtn);
    layout->addWidget(openFileBtn);

	// Show Shopping Bag Table button
	layout->addWidget(showBagTableButton);
    bagModel = new ShoppingBagModel(user_service);
    bagTableView = new QTableView();
    bagTableView->setModel(bagModel);
    bagTableView->hide();
    layout->addWidget(bagTableView);

    this->setLayout(layout);
   
	connect(filterBtn, &QPushButton::clicked, this, &UserWindow::filterTrenchCoats);
	connect(nextBtn, &QPushButton::clicked, this, &UserWindow::displayNextTrenchCoat);
	connect(addBtn, &QPushButton::clicked, this, &UserWindow::addToBasket);
	connect(basketBtn, &QPushButton::clicked, this, &UserWindow::displayShoppingBasket);    
	connect(openFileBtn, &QPushButton::clicked, this, &UserWindow::openShoppingBasketFile);
	connect(showBagTableButton, &QPushButton::clicked, this, &UserWindow::showShoppingBagTable);

    // Disable the Next and Add to Basket buttons initially
	nextBtn->setEnabled(false);
	addBtn->setEnabled(false);
}

