#pragma once
#include <QWidget>
#include <QGraphicsScene>
#include <QGraphicsView>
#include <QMap>
#include "TrenchCoat.h"

class BarChartWidget : public QWidget
{
    Q_OBJECT

public:
    explicit BarChartWidget(QWidget* parent = nullptr);
    void setData(const std::vector<TrenchCoat>& coats);

private:
    QGraphicsScene* scene;
    QGraphicsView* view;

    void drawChart();
    QVector<QPair<QString, int>> chartData;
};

