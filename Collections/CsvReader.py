from Collections.Player import Player
import os

class CsvReader():

    def __init__(self, filename, ):
        self.__filename = filename

    def get_filename(self):
        return self.__filename

    def read(self, list):
        with open(self.__filename, "r") as file:
            output = []
            for line in file:
                splitted_line = line.strip()
                tupple = splitted_line.split(";")
                if tupple[0] == "NACHNAME":
                    continue
                else:
                    for mttv_player in list:
                        if tupple[2] == str(mttv_player):
                            player = Player(tupple[0], tupple[1], tupple[2], tupple[4])
                            output.append(player.get_data())
            return output

    def delete(self):
        if os.path.exists(self.__filename):
            os.remove(self.__filename)
            print("Die Datei " + str(self.get_filename()) + " wurde gelöscht")
        else:
            print("The file does not exist")