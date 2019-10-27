from Datenbank_Funktionen import select_all_players
from helpfunctions.tuple_to_list import tuple_to_list
from Collections.CsvReader import CsvReader
from Collections.Database import DB
class MttvKader():

    def __init__(self, filename_female_csv, filename_male_csv, ):
        self.__filename_female_csv = filename_female_csv
        self.__filename_male_csv = filename_male_csv

    def update_execute(self):

        kader_player_tuple = select_all_players.select_all_players()
        kader_player_list = tuple_to_list(kader_player_tuple)

        # csv_reader_male = CsvReader.CsvReader("data/elo-rankings_gender-male_20190910.csv")
        csv_reader_male = CsvReader(self.__filename_male_csv)
        csv_list_male = csv_reader_male.read(kader_player_list)

        # csv_reader_female = CsvReader.CsvReader("data/elo-rankings_gender-female_20190910.csv")
        csv_reader_female = CsvReader(self.__filename_female_csv)
        csv_list_female = csv_reader_female.read(kader_player_list)

        db = DB()
        db.update(csv_list_male)
        db.update(csv_list_female)

        csv_reader_male.delete()
        csv_reader_female.delete()

