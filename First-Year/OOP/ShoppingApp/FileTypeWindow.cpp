#include "FileTypeWindow.h"
#include "Qlabel"

FileTypeWindow::FileTypeWindow(QWidget* parent) : QWidget(parent) {
    this->setWindowTitle("Select File Type");
    this->resize(800, 600);

    auto* layout = new QHBoxLayout;

    auto* typeLabel = new QLabel("Choose output format for shopping bag(CSV/HTML): ");
    auto* csvButton = new QPushButton("CSV");
    auto* htmlButton = new QPushButton("HTML");

    layout->addWidget(typeLabel);
    layout->addWidget(csvButton);
    layout->addWidget(htmlButton);

    this->setLayout(layout);

    connect(csvButton, &QPushButton::clicked, this, &FileTypeWindow::chooseCSV);
    connect(htmlButton, &QPushButton::clicked, this, &FileTypeWindow::chooseHTML);
}

void FileTypeWindow::chooseHTML()
{
    this->type = "HTML";
    this->close();
}

void FileTypeWindow::chooseCSV()
{
    this->type = "CSV";
    this->close();
}

std::string FileTypeWindow::getType() const
{
	return this->type;
}

