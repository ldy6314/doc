from mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
import sys
from docopt import generate_from_data
from excelopt import get_execl_info
import traceback
import jinja2


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.choose_data_button.clicked.connect(self.select_data_file)
        self.choose_template_button.clicked.connect(self.select_template_file)
        self.choose_output_button.clicked.connect(self.select_output_path)
        self.generate_button.clicked.connect(self.generate_document)

    def select_data_file(self):
        filename, ok = QFileDialog.getOpenFileName(filter='(*.xlsx)')
        if ok:
            self.data_path.setText(filename)

    def select_template_file(self):
        filename, ok = QFileDialog.getOpenFileName(filter='(*.docx)')
        if ok:
            self.template_path.setText(filename)

    def select_output_path(self):
        dir_name = QFileDialog.getExistingDirectory()
        self.output_path.setText(dir_name)

    def generate_document(self):
        template_file = self.template_path.text()
        out_name = self.output_filename.text()
        data_file = self.data_path.text()
        start_row = self.start_row.value()
        end_row = self.end_row.value()
        if template_file and out_name and data_file:
            output_file = self.output_path.text() + '/' + out_name + '.docx'
            try:
                data_list = get_execl_info(data_file, start_row, end_row)
            except Exception as e:
                e
                self.run_infos.setText(str(traceback.format_exc()))
            try:
                generate_from_data(template_file, output_file, data_list)

            except jinja2.exceptions.TemplateSyntaxError as e:
                self.run_infos.setText('模板格式错误\n' + '详情:' + str(e))

            except Exception as e:
                e
                self.run_infos.setText(str(traceback.format_exc()))
            else:
                success_info = "文件 {} 生成成功".format(output_file)
                self.run_infos.setText(success_info)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
