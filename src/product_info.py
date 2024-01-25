class ProductInfo:
    def __init__(self, protein: float, fats: float, carbo: float):
        self.protein = protein
        self.fats = fats
        self.carbo = carbo

    def __str__(self):
        return (f"+----------PRODUCT INFO----------+\n"
                f"Proteins: {self.protein}\n"
                f"Fats: {self.fats}\n"
                f"Carbohydrates: {self.carbo}\n"
                f"+----------------------------+\n")
