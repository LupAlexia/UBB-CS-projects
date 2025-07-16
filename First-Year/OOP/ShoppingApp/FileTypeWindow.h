#pragma once
#include <QWidget>
#include <QPushButton>
#include <QVBoxLayout>
#include <QString>

class FileTypeWindow : public QWidget {
    Q_OBJECT

public:
    FileTypeWindow(QWidget* parent = nullptr);
    std::string getType() const;

private slots:
    void chooseCSV();
    void chooseHTML();
private:
    std::string type;
};