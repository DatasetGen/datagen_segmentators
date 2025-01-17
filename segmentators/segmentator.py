from abc import abstractmethod, ABC
from enum import Enum

from pydantic import BaseModel
from typing import List, Tuple
from PIL import Image


class BoundingBox(BaseModel):
    x_0: int
    y_0: int
    x_1: int
    y_1: int


class Segmentation(BaseModel):
    points: List[Tuple[int, int]]

class Result(BaseModel):
    bounding_boxes: List[BoundingBox]
    segmentations: List[Segmentation]

class Segmentator(ABC):
    @abstractmethod
    def segment(self, image: Image.Image) -> Result:
        ...