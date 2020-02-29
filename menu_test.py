from notebook import Notebook, Note
from menu import Menu

if __name__ == "__main__":
    m = Menu()
    print(dir(m))
    print(m.__dict__)
    print(m.__dir__)
    print(isinstance("display_menu", object))
    print(m.__init__)
    print(m.__delattr__)
    print(isinstance('modify_note', Menu))
    print(isinstance('modify_note', Notebook))