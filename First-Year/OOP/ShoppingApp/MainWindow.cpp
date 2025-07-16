#include "MainWIndow.h"
#include "UserWindow.h"
#include "AdminWindow.h"

MainWindow::MainWindow(Service& service, UserService& user_service, QWidget* parent) : QWidget(parent), service(service), user_service(user_service)
{
	this->setWindowTitle("Proper Trench Coats - Main Menu");
	this->resize(800, 600);

	modeLabel = new QLabel("Choose mode:");
	adminButton = new QPushButton("Administrator Mode");
	adminButton->setFixedSize(250, 50);
	adminButton->setStyleSheet("background-color: #2c3e50; color: white; padding: 10px 20px; font - size: 16px;border - radius: 8px; ");
	userButton = new QPushButton("User Mode");
	userButton->setFixedSize(250, 50);
	userButton->setStyleSheet("background-color: #2c3e50; color: white; padding: 10px 20px; font - size: 16px;border - radius: 8px;");

	auto* layout = new QHBoxLayout;
	layout->addWidget(modeLabel);
	layout->addWidget(adminButton);
	layout->addWidget(userButton);
	setLayout(layout);

	connect(adminButton, &QPushButton::clicked, this, &MainWindow::openAdmin);
	connect(userButton, &QPushButton::clicked, this, &MainWindow::openUser);
}

void MainWindow::openAdmin()
{
	auto* adminWin = new AdminWindow(this->service);
	adminWin->show();
}

void MainWindow::openUser()
{
	auto* userWin = new UserWindow( this->user_service);
	userWin->show();
}
