#include <iostream>
#include "MainWIndow.h"
#include <QApplication>
#include "FileTypeWindow.h"
//#include "Tests.h"
#include "Service.h"
#include "Service_user.h"
#include "BarChartWidget.h"
using namespace std;

int main(int argc, char* argv[]) {
	//Tests tests;
	//tests.testAll();
	QApplication app(argc, argv);
	FileRepository coats_repo ("TrenchCoats.txt" );
	Repository basket_repo;
	Service service { coats_repo };
	UserService user_service{ coats_repo, basket_repo };

	//Show bar chart with the number of trench coats per size
	BarChartWidget chart;
	chart.setData(service.getAllTrenchCoats());
	chart.show();

	//wait for the chart to be closed
	while (chart.isVisible()) {
		app.processEvents();
	}

	// Choose file type for the shopping bag
	FileTypeWindow ftWindow;
	ftWindow.show();
	while (ftWindow.isVisible()) { // wait for the user to select a file type before creating the main window
		app.processEvents();
	}

	if (ftWindow.getType() == "CSV") {
		user_service.setFileWriter(std::make_unique<CSVFileWriter>("shopping_bag.csv"));
	}
	else if (ftWindow.getType() == "HTML") {
		user_service.setFileWriter(std::make_unique<HTMLFileWriter>("shopping_bag.html"));
	}

	MainWindow mainWindow{ service, user_service };
	mainWindow.show();

	return app.exec();
}