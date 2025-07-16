#pragma once
#include <QAbstractTableModel>
#include "Service_user.h"


class ShoppingBagModel : public QAbstractTableModel {  // inherits from QAbstractTableModel to represent the shopping bag in a table format
    Q_OBJECT
private:
	UserService& userService; // reference to the UserService to access the shopping bag data

public:
    ShoppingBagModel(UserService& userService, QObject* parent = nullptr);

    int rowCount(const QModelIndex& parent = QModelIndex()) const override;
    int columnCount(const QModelIndex& parent = QModelIndex()) const override;
    QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;
    QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;

    void update();
};
