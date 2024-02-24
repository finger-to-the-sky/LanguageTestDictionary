from tkinter import Tk, Frame, Label, Text, Button
from app.functions import other_functionality, set_languages, test_mode_activate
from app.text_field_functionality import russian_add_hotkeys, create_context_menu
from app.config import TITLE, SIZE_WINDOW


root = Tk()
root.title(TITLE)
root.geometry(SIZE_WINDOW)

frame = Frame(root)

# Header
label = Label(root, text=f'Добро пожаловать в {TITLE}',
              font=('Helvetica', 20))
label.pack()

# Temporary function for buttons
test_mode_button = Button(frame, text='Запустить режим тестирования', command=lambda: test_mode_activate(root=root))
other_functionality(frame)
test_mode_button.grid(row=0, column=4, padx=20)

# Text Fields
user_text_widget = Text(root, width=100, height=10)
translated_text_widget = Text(root, width=100, height=10)

# Function for creating the necessary components for translation
set_languages(root=root, button_frame=frame, user_text=user_text_widget, translated_text=translated_text_widget)

# Text Fields
user_text_widget.pack(pady=(15, 0))
translated_text_widget.pack(pady=(15, 0))

# Hotkeys for russian keyboard
russian_add_hotkeys(root=root, text_widgets=(user_text_widget, translated_text_widget))

# Create context menu for right mouse button
create_context_menu(root=root, text_widgets=(user_text_widget, translated_text_widget))

root.mainloop()
