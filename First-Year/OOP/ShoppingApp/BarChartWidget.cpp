#include "BarChartWidget.h"
#include <QGraphicsRectItem>
#include <QGraphicsTextItem>
#include <QVBoxLayout>
#include <QPen>
#include <QBrush>
#include <algorithm>

BarChartWidget::BarChartWidget(QWidget* parent) : QWidget(parent), scene(new QGraphicsScene(this)), view(new QGraphicsView(scene, this))
{
    view->setFixedSize(800, 600);
    auto layout = new QVBoxLayout(this);
    layout->addWidget(view);
    setLayout(layout);
}

void BarChartWidget::setData(const std::vector<TrenchCoat>& coats)
{
    QStringList sizeOrder = { "XS", "S", "M", "L", "XL" };
    QMap<QString, int> tempCounts;

    for (const auto& coat : coats) {
        QString size = QString::fromStdString(coat.getSize());
        tempCounts[size]++;
    }

    chartData.clear();
    for (const QString& size : sizeOrder) {
        if (tempCounts.contains(size)) {
            chartData.append({ size, tempCounts[size] });
        }
    }

    drawChart();
}



void BarChartWidget::drawChart()
{
    scene->clear();

    int chartLeft = 100;
    int chartBottom = 400; 
    int barWidth = 40;
    int spacing = 30;
    int maxHeight = 300;

    if (chartData.isEmpty()) return;

    int maxValue = 0;
    for (const auto& pair : chartData) {
        maxValue = std::max(maxValue, pair.second);
    }

    for (int i = 0; i <= maxValue; ++i) {
        int y = chartBottom - (static_cast<double>(i) / maxValue * maxHeight); 
        scene->addLine(chartLeft - 5, y, chartLeft, y);
        QGraphicsTextItem* label = scene->addText(QString::number(i));
        label->setPos(chartLeft - 40, y - 10);
    }

    QGraphicsTextItem* yLabel = scene->addText("Number of trench coats");
    yLabel->setRotation(-90);
    yLabel->setPos(chartLeft - 70, chartBottom - maxHeight / 2);

    QGraphicsTextItem* xLabel = scene->addText("Sizes");
    xLabel->setPos(chartLeft + (chartData.size() * (barWidth + spacing)) / 2 - 20, chartBottom + 20);

    int x = chartLeft + 20;

    for (const auto& pair : chartData) {
        const QString& size = pair.first;
        int value = pair.second;

		int barHeight = static_cast<int>((double)value / maxValue * maxHeight); // calculate bar height
		int y = chartBottom - barHeight; // calculate y position

		// Draw the bar
        scene->addRect(x, y, barWidth, barHeight, QPen(Qt::black), QBrush(Qt::green));

		// Draw the size label
        QGraphicsTextItem* sizeLabel = scene->addText(size);
        sizeLabel->setPos(x, chartBottom + 10);

        x += barWidth + spacing;
    }
}
