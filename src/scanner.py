import enum
import easyocr as ocr
import cv2


class Language(enum.Enum):
    ENGLISH = "en"
    RUSSIAN = "ru"


class ImageScanner:

    def __init__(self, lang: list[Language], gpu: bool = False):
        self.reader = ocr.Reader([token.value for token in lang], gpu=gpu)

    def scan_image(self, image_path: str, verbose: bool = False) -> list[str]:
        image = cv2.imread(image_path)
        extracted_text = self.reader.readtext(image, paragraph=True)
        if verbose:
            for (bbox, text) in extracted_text:
                print(f"[INFO] : {text}")
                (tl, tr, br, bl) = bbox
                tl = (int(tl[0]), int(tl[1]))
                br = (int(br[0]), int(br[1]))
                cv2.rectangle(image, tl, br, (0, 255, 0), 2)
                cv2.putText(image, text, (tl[0], tl[1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.imshow("Image", image)
            cv2.waitKey(0)
        return [text for _, text in extracted_text]
