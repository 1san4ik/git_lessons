# Задание 1
# Создайте класс Editor, который содержит методы view_document и edit_document. Пусть метод
# edit_document выводит на экран информацию о том, что редактирование документов недоступно для
# бесплатной версии. Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте экземпляр класса ProEditor,
# иначе Editor. Вызовите методы просмотра и редактирования документов.

class Editor:
    def view_document(self):
        print("Вы можете просматривать документ.")

    def edit_document(self):
        print("Редактирование документов недоступно для бесплатной версии")


class ProEditor(Editor):
    def edit_document(self):
        print("Вы можете редактировать документ.")


def main():
    key = input('Введите лицензионный ключ: ')
    if key == 'qqqwww777':
        print('Ключ принят!')
        editor = ProEditor()
    else:
        print('Ключ неверный!')
        editor = Editor()

    editor.view_document()
    editor.edit_document()


if __name__ == '__main__':
    main()
