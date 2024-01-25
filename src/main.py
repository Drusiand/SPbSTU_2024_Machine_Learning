from scanner import ImageScanner, Language
from parser import Parser

from person_info import PersonInfo, Goal, ActivityLevel, Gender

import pandas as pd
from regressor import Regressor


def test():
    # df = pd.read_csv("../data/dataset/dataset.csv")
    # regressor = Regressor(df)
    # regressor.prepare_model(tune_parameters=False)
    #
    # person_info = PersonInfo(age=23,
    #                          gender=Gender.MALE.value,
    #                          height=180,
    #                          weight=75,
    #                          activity_level=ActivityLevel.MILD.value,
    #                          goal=Goal.WEIGHT_LOSE.value)

    for i in range(10):

        scanner = ImageScanner([Language.RUSSIAN])
        parser = Parser()
        product_info = parser.parse(scanner.scan_image(f"../data/img/product_{i+1}.jpg"))
        print(i)
        print(product_info)

    # regressor.predict(person_info, product_info)


if __name__ == '__main__':
    test()
