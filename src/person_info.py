from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class ActivityLevel(Enum):
    NO = "no"
    SEDENTARY = "sedentary"
    RARE = "rare"
    MILD = "mild"
    LOW_INTENSE = "lowintense"
    INTENSE = "intense"
    VERY_INTENSE = "veryintense"


class Goal(Enum):
    MAINTAIN = "maintain"
    MILD_LOSE = "mildlose"
    WEIGHT_LOSE = "weightlose"
    EXTREME_LOSE = "extremelose"
    MILD_GAIN = "mildgain"
    WEIGHT_GAIN = "weightgain"
    EXTREME_GAIN = "extremegain"


class PersonInfo:
    def __init__(self, age: int, gender: Gender, height: int, weight: int, activity_level: ActivityLevel, goal: Goal):
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.activity_level = activity_level
        self.goal = goal

    def __str__(self):
        return (f"+----------PERSON INFO----------+\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Height: {self.height}\n"
                f"Weight: {self.weight}\n"
                f"Activity level: {self.activity_level}\n"
                f"Goal: {self.goal}\n"
                f"+-------------------------------+\n")
