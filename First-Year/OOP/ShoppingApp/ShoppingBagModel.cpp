#include "ShoppingBagModel.h"


ShoppingBagModel::ShoppingBagModel(UserService& userService, QObject* parent)
    : QAbstractTableModel(parent), userService(userService) {
}

int ShoppingBagModel::rowCount(const QModelIndex& /*parent*/) const {
    return static_cast<int>(userService.getBag().size());
}

int ShoppingBagModel::columnCount(const QModelIndex& /*parent*/) const {
    return 5; // Size, Colour, Price, Quantity, Photograph
}

QVariant ShoppingBagModel::data(const QModelIndex& index, int role) const {
    if (role != Qt::DisplayRole)
        return QVariant();

    const auto& bag = userService.getBag();
    const auto& coat = bag.at(index.row());

    switch (index.column()) {
    case 0: return QString::fromStdString(coat.getSize());
    case 1: return QString::fromStdString(coat.getColour());
    case 2: return coat.getPrice();
    case 3: return coat.getQuantity();
    case 4: return QString::fromStdString(coat.getPhotograph());
    default: return QVariant();
    }
}

QVariant ShoppingBagModel::headerData(int section, Qt::Orientation orientation, int role) const {
    if (role != Qt::DisplayRole)
        return QVariant();

    if (orientation == Qt::Horizontal) {
        switch (section) {
        case 0: return "Size";
        case 1: return "Colour";
        case 2: return "Price";
        case 3: return "Quantity";
        case 4: return "Photograph";
        default: return QVariant();
        }
    }
    return QVariant();
}

void ShoppingBagModel::update() {
    beginResetModel();
    endResetModel();
}
