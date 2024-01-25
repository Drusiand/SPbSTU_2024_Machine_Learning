from product_info import ProductInfo
from fuzzywuzzy import fuzz

TEXT_DELIMITER = ' '
NUMBER_DELIMITER = ','
DOT_DELIMITER = '.'


class Parser:

    def __init__(self):
        self.protein_keywords = ["белок", "белка", "белки", "белков"]
        self.fats_keywords = ["жир", "жиры", "жира", "жиров"]
        self.carbo_keywords = ["углевод", "углеводы", "углевода", "углеводов"]

    @staticmethod
    def __is_valid_char(char: str) -> bool:
        return char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ","]

    def __find_next_number(self, tokens: list[str], start_position: int):
        i = start_position
        begin_flag = True
        break_flag = False
        number = ""
        while True:
            token = tokens[i]
            for char in token:
                if self.__is_valid_char(char):
                    begin_flag = False
                    number += char
                else:
                    if not begin_flag:
                        break_flag = True
            if break_flag:
                break
            i += 1
        return number

    @staticmethod
    def __validate_number(raw_str: str) -> float:
        processed_str = raw_str.replace(NUMBER_DELIMITER, DOT_DELIMITER)
        result = float(processed_str) / 10 if float(processed_str) > 10 else float(processed_str)
        return result

    @staticmethod
    def __find_close_word(tokens: list[str], word: str):
        for i, token in enumerate(tokens):
            if fuzz.ratio(word, token.lower()) > 60:
                print(token)
                return i
        return None

    def parse(self, text: list[str]) -> ProductInfo:
        protein, fats, carbo = 0, 0, 0
        for paragraph in text:
            tokens = paragraph.split(TEXT_DELIMITER)
            for keyword in self.protein_keywords:
                protein_index = self.__find_close_word(tokens, keyword)
                if protein_index is None:
                    break
                raw = self.__find_next_number(tokens, protein_index + 1)
                protein = self.__validate_number(raw)
                self.protein_keywords.clear()
            for keyword in self.fats_keywords:
                fat_index = self.__find_close_word(tokens, keyword)
                if fat_index is None:
                    break
                raw = self.__find_next_number(tokens, fat_index + 1)
                fats = self.__validate_number(raw)
                self.fats_keywords.clear()
            for keyword in self.carbo_keywords:
                carbo_index = self.__find_close_word(tokens, keyword)
                if carbo_index is None:
                    break
                raw = self.__find_next_number(tokens, carbo_index + 1)
                carbo = self.__validate_number(raw)
                self.carbo_keywords.clear()
        return ProductInfo(protein, fats, carbo)

    # def parse(self, text: list[str]) -> ProductInfo:
    #     protein, fats, carbo = 0, 0, 0
    #     for paragraph in text:
    #         tokens = paragraph.split(TEXT_DELIMITER)
    #         for i, token in enumerate(tokens):
    #             for keyword in self.protein_keywords:
    #                 protein_index = self.find_close_word(tokens, keyword)
    #                 raw = self.__find_next_number(tokens, protein_index + 1)
    #                 protein = self.__validate_number(raw)
    #             # if token.lower() in self.protein_keywords:
    #
    #             # elif token.lower() in self.fats_keywords:
    #             #     raw = self.__find_next_number(tokens, i + 1)
    #             #     fats = self.__validate_number(raw)
    #             # elif token.lower() in self.carbo_keywords:
    #             #     raw = self.__find_next_number(tokens, i + 1)
    #             #     carbo = self.__validate_number(raw)
    #         return ProductInfo(protein, fats, carbo)
