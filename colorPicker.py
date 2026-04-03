from PySide6.QtWidgets import QColorDialog


def pick_color():

    color = QColorDialog.getColor()

    if color.isValid():
        print(color.name())
        return color.name()
    else:
        return "#FFFFFF"