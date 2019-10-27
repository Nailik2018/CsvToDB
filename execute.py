from Collections.MttvKader import MttvKader

filename_female_csv = "data/elo-rankings_gender-female_20191010.csv"
filename_male_csv = "data/elo-rankings_gender-male_20191010.csv"

mttv_kader = MttvKader(filename_female_csv, filename_male_csv)
mttv_kader.update_execute()
