from pickle import dump, load

# Manages saving and loading
class SaveManager:
    def __init__(self):
        self.file_name = "Saves/save.txt"
        self.file_contents = None

    # Opens save file and return contents as a dictionary
    def get_save(self):
        self.open_save_file()
        return self.file_contents

    # Uses pickle module to open save file
    def open_save_file(self):
        with open(self.file_name, "rb") as file:
            self.file_contents = load(file)
    
    # Uses pickle module to save dictionary to file
    def write_to_save_file(self, save):
        with open(self.file_name, "wb") as file:
            dump(save, file)

    # Delete save file
    def clear_save_file(self):
        with open(self.file_name, "wb") as file:
            dump("", file)


