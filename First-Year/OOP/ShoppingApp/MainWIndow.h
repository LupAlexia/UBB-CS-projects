#pragma once
#include <QWidget>
#include <QPushButton>
#include <QVBoxLayout>
#include <Qlabel>
#include "Service.h"
#include "Service_user.h"

class MainWindow : public QWidget {
	Q_OBJECT 

public:
	MainWindow(Service& service, UserService& user_service, QWidget* parent = nullptr);
private slots: // slots are functions that can be connected to signals
	void openAdmin();
	void openUser();
private: // UI elements
	QPushButton* adminButton;
	QPushButton* userButton;
	QLabel* modeLabel;

	Service& service;
	UserService& user_service;
};