import json
import sys

from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QTextEdit, \
    QApplication

from WindowPositionManipulations import center_window



class edit_picks_json_dashboard(QWidget):
    def __init__(self):
        super().__init__()
        from PySide6.QtWidgets import QScrollArea

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        self.main_layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(self.main_layout)

        scroll.setWidget(container)

        outer_layout = QVBoxLayout(self)
        outer_layout.addWidget(scroll)
        self.setMinimumSize(600, 600)
        self.setWindowTitle("Edit Clinical Key Words")
        center_window(self)
        with open ("clinical_triggers.json","r") as file:
            clinical_keys_dic = json.load(file)
        clinical_keys_dic = dict(sorted(clinical_keys_dic.items()))
        containers_list = []
        self.contents_widgets_list=[]
        for i,key in enumerate(clinical_keys_dic.keys()):
            self.temp_layout = QGridLayout()



            temp_key_word_line_edit = QLineEdit()
            temp_key_word_line_edit.setReadOnly(False)
            temp_key_word_line_edit.setText(key)

            temp_aliases_text_edit = QTextEdit()
            temp_aliases_text_edit.setReadOnly(False)
            for value in clinical_keys_dic[key]:
                temp_aliases_text_edit.append(value)
            self.temp_layout.addWidget(temp_key_word_line_edit,0,0)
            self.temp_layout.addWidget(temp_aliases_text_edit,0,1)

            #here u can solve the confusion of containers and contents
            containers_list.append([self.temp_layout])
            self.contents_widgets_list.append([temp_key_word_line_edit,temp_aliases_text_edit])

            self.main_layout.addLayout(self.temp_layout)
        self.add_button=QPushButton("Add Field")
        self.add_button.setEnabled(True)
        self.update_button = QPushButton("Update")
        self.update_button.setEnabled(True)

        self.main_layout.addWidget(self.add_button)
        self.main_layout.addWidget(self.update_button)
        self.add_button.clicked.connect(self.add_field)
        self.update_button.clicked.connect(self.update_json)
    def add_field(self):
        self.main_layout.removeWidget(self.add_button)
        self.main_layout.removeWidget(self.update_button)
        temp_layout = QGridLayout()
        temp_key_word_line_edit = QLineEdit()
        temp_key_word_line_edit.setReadOnly(False)

        temp_aliases_text_edit = QTextEdit()
        temp_aliases_text_edit.setReadOnly(False)
        self.contents_widgets_list.append([temp_key_word_line_edit,temp_aliases_text_edit])
        temp_layout.addWidget(temp_key_word_line_edit,0,0)
        temp_layout.addWidget(temp_aliases_text_edit,0,1)
        self.main_layout.addLayout(temp_layout)
        self.main_layout.addWidget(self.add_button)
        self.main_layout.addWidget(self.update_button)
    def update_json(self):
        new_dic={}
        for content_list in self.contents_widgets_list:#list of two element lists [0]=lined edit for key [1]=text edit for aliases
            if content_list[0].text().strip() and content_list[1].toPlainText().strip():
                lines = [line.strip() for line in content_list[1].toPlainText().split("\n")]
                new_dic[content_list[0].text().strip()]=lines
        new_dic = dict(sorted(new_dic.items()))
        with open('clinical_triggers.json','w') as file:
            json.dump(new_dic,file,indent=4)
        print (new_dic)
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window=edit_picks_json_dashboard()
    window.show()
    sys.exit(app.exec())



