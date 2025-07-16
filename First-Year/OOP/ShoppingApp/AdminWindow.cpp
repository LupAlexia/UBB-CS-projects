#include "AdminWindow.h"
#include <QMessageBox>

AdminWindow::AdminWindow(Service& service, QWidget* parent) : QWidget(parent), service(service)
{
    this->setWindowTitle("Administrator Panel");
    this->resize(800, 600);
    initUI();
    populateTable();
}

void AdminWindow::addTrenchCoat()
{
	std::string size = sizeInput->text().toStdString(); 
	std::string color = colorInput->text().toStdString();
	double price = priceInput->text().toDouble();
	int quantity = qtyInput->text().toInt();
	std::string photograph = photoInput->text().toStdString();

    try {
		service.addTrenchCoat(size, color, price, quantity, photograph);
		QMessageBox::information(this, "Success", "Trench coat added successfully!");
		populateTable();
    }
    catch (const DuplicateTrenchCoatException& e) {
		QMessageBox::critical(this, "Error", e.what());
	}
	catch (const ValidationException& e) {
		QMessageBox::critical(this, "Error", e.what());
	}

    sizeInput->clear();
    colorInput->clear();
    priceInput->clear();
    qtyInput->clear();
    photoInput->clear();
}

void AdminWindow::deleteTrenchCoat()
{
    std::string size = sizeInput->text().toStdString();
    std::string color = colorInput->text().toStdString();

    try {
        service.removeTrenchCoat(size, color);
        QMessageBox::information(this, "Success", "Trench coat removed successfully!");
        populateTable();
    }
    catch (const TrenchCoatNotFoundException& e) {
        QMessageBox::critical(this, "Error", e.what());
    }
    catch (const ValidationException& e) {
        QMessageBox::critical(this, "Error", e.what());
    }
    sizeInput->clear();
    colorInput->clear();
    priceInput->clear();
    qtyInput->clear();
    photoInput->clear();
}

void AdminWindow::updateTrenchCoat()
{
	std::string size = sizeInput->text().toStdString();
	std::string color = colorInput->text().toStdString();
	double price = priceInput->text().toDouble();
	int quantity = qtyInput->text().toInt();
	std::string photograph = photoInput->text().toStdString();
	try {
		service.updateTrenchCoat(size, color, price, quantity, photograph);
		QMessageBox::information(this, "Success", "Trench coat updated successfully!");
		populateTable();
	}
	catch (const TrenchCoatNotFoundException& e) {
		QMessageBox::critical(this, "Error", e.what());
	}
	catch (const ValidationException& e) {
		QMessageBox::critical(this, "Error", e.what());
	}
    sizeInput->clear();
    colorInput->clear();
    priceInput->clear();
    qtyInput->clear();
    photoInput->clear();
}

void AdminWindow::undoAction()
{
    service.undo();
    populateTable();
}

void AdminWindow::redoAction()
{
	service.redo();
	populateTable();
}

void AdminWindow::populateTable()
{
    table->setRowCount(0);
    const auto& coats = service.getAllTrenchCoats();
    int row = 0;
    for (const auto& coat : coats) {
        table->insertRow(row);
        table->setItem(row, 0, new QTableWidgetItem(QString::fromStdString(coat.getSize())));
        table->setItem(row, 1, new QTableWidgetItem(QString::fromStdString(coat.getColour())));
        table->setItem(row, 2, new QTableWidgetItem(QString::number(coat.getPrice())));
        table->setItem(row, 3, new QTableWidgetItem(QString::number(coat.getQuantity())));
        table->setItem(row, 4, new QTableWidgetItem(QString::fromStdString(coat.getPhotograph())));
        row++;
    }
}

void AdminWindow::initUI()
{
    table = new QTableWidget();
    table->setColumnCount(5);
    QStringList headers = { "Size", "Color", "Price", "Quantity", "Photo" };
    table->setHorizontalHeaderLabels(headers);

    sizeInput = new QLineEdit();
    colorInput = new QLineEdit();
    priceInput = new QLineEdit();
    qtyInput = new QLineEdit();
    photoInput = new QLineEdit();

    addButton = new QPushButton("Add");
    delButton = new QPushButton("Delete");
    updateButton = new QPushButton("Update");
    undoButton = new QPushButton("Undo (Ctrl+Z)");
    redoButton = new QPushButton("Redo (Ctrl+Y)");

    sizeLabel = new QLabel("Size: ");
    colorLabel = new QLabel("Color: ");
    priceLabel = new QLabel("Price: ");
    qtyLabel = new QLabel("Quantity: ");
    photoLabel = new QLabel("Photo: ");

    auto* formLayout = new QHBoxLayout;
    formLayout->addWidget(sizeInput);
    formLayout->addWidget(colorInput);
    formLayout->addWidget(priceInput);
    formLayout->addWidget(qtyInput);
    formLayout->addWidget(photoInput);

    auto* buttonLayout = new QHBoxLayout;
    buttonLayout->addWidget(addButton);
    buttonLayout->addWidget(delButton);
    buttonLayout->addWidget(updateButton);

	auto* labelLayout = new QHBoxLayout;
	labelLayout->addWidget(sizeLabel);
	labelLayout->addWidget(colorLabel);
	labelLayout->addWidget(priceLabel);
	labelLayout->addWidget(qtyLabel);
	labelLayout->addWidget(photoLabel);

    auto* buttonLayout2 = new QHBoxLayout;
	buttonLayout2->addWidget(undoButton);
	buttonLayout2->addWidget(redoButton);

    auto* mainLayout = new QVBoxLayout;
    mainLayout->addWidget(table);
    mainLayout->addLayout(labelLayout);
    mainLayout->addLayout(formLayout);
    mainLayout->addLayout(buttonLayout);
    mainLayout->addLayout(buttonLayout2);

    setLayout(mainLayout);

    connect(addButton, &QPushButton::clicked, this, &AdminWindow::addTrenchCoat);
    connect(delButton, &QPushButton::clicked, this, &AdminWindow::deleteTrenchCoat);
    connect(updateButton, &QPushButton::clicked, this, &AdminWindow::updateTrenchCoat);
	connect(undoButton, &QPushButton::clicked, this, &AdminWindow::undoAction);
	connect(redoButton, &QPushButton::clicked, this, &AdminWindow::redoAction);
	undoButton->setShortcut(QKeySequence(Qt::CTRL | Qt::Key_Z));
	redoButton->setShortcut(QKeySequence(Qt::CTRL | Qt::Key_Y));

	undoButton->setStyleSheet("background-color: #2c3e50; color: white; padding: 10px 20px; font-size: 16px; border-radius: 8px;");
	redoButton->setStyleSheet("background-color: #2c3e50; color: white; padding: 10px 20px; font-size: 16px; border-radius: 8px;");
}
