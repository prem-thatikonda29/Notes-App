import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QLabel, QDialog

class NotesApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Simple Notes App')
        self.setGeometry(100, 100, 400, 400)

        # Text area
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Write your notes here...")

        # Save and View button
        save_button = QPushButton('Save', self)
        save_button.clicked.connect(self.save_notes)

        view_button = QPushButton('View Notes', self)
        view_button.clicked.connect(self.view_notes)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(save_button)
        layout.addWidget(view_button)

        self.setLayout(layout)

    def save_notes(self):
        notes = self.text_edit.toPlainText()

        if notes:
            with open('notes.txt', 'a') as file: 
                file.write(notes + '\n')  
            QMessageBox.information(self, 'Saved', 'Notes saved successfully!')
        else:
            QMessageBox.warning(self, 'Empty Notes', 'Please write something before saving.')
    
    def view_notes(self):
        try:
            with open('notes.txt', 'r') as file:
                notes = file.read()
                if notes:
                    view_dialog = QDialog(self)
                    view_dialog.setWindowTitle('View Notes')
                    view_dialog.setGeometry(200, 200, 400, 400)

                    notes_label = QLabel(notes, view_dialog)
                    notes_label.setWordWrap(True)

                    layout = QVBoxLayout(view_dialog)
                    layout.addWidget(notes_label)

                    view_dialog.setLayout(layout)
                    view_dialog.exec_()
                else:
                    QMessageBox.information(self, 'No Notes', 'No notes found. Write some first!')
        except FileNotFoundError:
            QMessageBox.warning(self, 'File Not Found', 'No notes found. Write some first!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    notes_app = NotesApp()
    notes_app.show()
    sys.exit(app.exec_())