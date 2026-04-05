import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton,  QTextEdit, \
    QApplication

from WindowPositionManipulations import center_window
from getBaseDir import get_base_dir
from jsonResolve import load_json, write_json


class edit_feeds_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit Feeds")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.feeds_list_text_edit = QTextEdit()
        self.Title_label = QLabel("paste new feeds or deleted feeds")
        self.Title_label.setAlignment(Qt.AlignCenter)
        self.update_button = QPushButton("Update")
        self.update_button.clicked.connect(self.update_feeds)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close)

        self.json_path=get_base_dir()+"feeds_list.json"
        self.feeds_list=load_json(self.json_path,"nofeed")
        for feed in self.feeds_list:
            self.feeds_list_text_edit.append(feed)



        self.layout.addWidget(self.Title_label, 0, 0, 1, 2)
        self.layout.addWidget(self.feeds_list_text_edit, 1, 0, 1, 2)
        self.layout.addWidget(self.update_button, 2, 0)
        self.layout.addWidget(self.cancel_button, 2,1)
        self.setFixedSize(900,self.sizeHint().height())

        center_window(self)

    def update_feeds(self):
        edited_feeds_list = self.feeds_list_text_edit.toPlainText().split("\n")

        edited_feeds_list = [x  for x in edited_feeds_list if x.strip()]
        print("new list pushed :\n","\n".join(edited_feeds_list))
        write_json(self.json_path,edited_feeds_list)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=edit_feeds_window()
    window.show()
    sys.exit(app.exec())



