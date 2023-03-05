# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u4e2d\u5b8b"])
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.template_path = QLineEdit(self.centralwidget)
        self.template_path.setObjectName(u"template_path")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.template_path.sizePolicy().hasHeightForWidth())
        self.template_path.setSizePolicy(sizePolicy)
        self.template_path.setMinimumSize(QSize(0, 30))
        self.template_path.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.template_path)

        self.choose_template_button = QToolButton(self.centralwidget)
        self.choose_template_button.setObjectName(u"choose_template_button")
        self.choose_template_button.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.choose_template_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.data_path = QLineEdit(self.centralwidget)
        self.data_path.setObjectName(u"data_path")
        self.data_path.setMinimumSize(QSize(0, 30))
        self.data_path.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.data_path)

        self.choose_data_button = QToolButton(self.centralwidget)
        self.choose_data_button.setObjectName(u"choose_data_button")
        self.choose_data_button.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.choose_data_button)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.start_row = QSpinBox(self.centralwidget)
        self.start_row.setObjectName(u"start_row")
        self.start_row.setMinimumSize(QSize(0, 30))
        self.start_row.setMaximum(999999)
        self.start_row.setValue(2)

        self.horizontalLayout_2.addWidget(self.start_row)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.label_7)

        self.end_row = QSpinBox(self.centralwidget)
        self.end_row.setObjectName(u"end_row")
        self.end_row.setMinimumSize(QSize(0, 30))
        self.end_row.setMaximum(999999)
        self.end_row.setValue(999999)

        self.horizontalLayout_2.addWidget(self.end_row)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.output_path = QLineEdit(self.centralwidget)
        self.output_path.setObjectName(u"output_path")
        sizePolicy.setHeightForWidth(self.output_path.sizePolicy().hasHeightForWidth())
        self.output_path.setSizePolicy(sizePolicy)
        self.output_path.setMinimumSize(QSize(0, 30))
        self.output_path.setReadOnly(True)

        self.horizontalLayout.addWidget(self.output_path)

        self.choose_output_button = QToolButton(self.centralwidget)
        self.choose_output_button.setObjectName(u"choose_output_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.choose_output_button.sizePolicy().hasHeightForWidth())
        self.choose_output_button.setSizePolicy(sizePolicy2)
        self.choose_output_button.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.choose_output_button)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.output_filename = QLineEdit(self.centralwidget)
        self.output_filename.setObjectName(u"output_filename")
        sizePolicy.setHeightForWidth(self.output_filename.sizePolicy().hasHeightForWidth())
        self.output_filename.setSizePolicy(sizePolicy)
        self.output_filename.setMinimumSize(QSize(0, 30))
        self.output_filename.setReadOnly(False)

        self.horizontalLayout.addWidget(self.output_filename)

        self.generate_button = QPushButton(self.centralwidget)
        self.generate_button.setObjectName(u"generate_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.generate_button.sizePolicy().hasHeightForWidth())
        self.generate_button.setSizePolicy(sizePolicy3)
        self.generate_button.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.generate_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.run_infos = QTextEdit(self.groupBox)
        self.run_infos.setObjectName(u"run_infos")
        self.run_infos.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.run_infos)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 2)

        self.horizontalLayout_5.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ldy word\u6587\u6863\u6279\u91cf\u751f\u6210\u5668", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u677f\u8def\u5f84", None))
        self.choose_template_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u8def\u5f84", None))
        self.choose_data_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u884c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u884c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u8def\u5f84", None))
        self.choose_output_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u6587\u4ef6\u540d", None))
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u4fe1\u606f", None))
    # retranslateUi

