from typing import Optional

from ultralytics import SAM
from segmentators.segmentator import Segmentator, Result, BoundingBox, Segmentation
from PIL import Image
import numpy as np


class SAM2Segmentator(Segmentator):
    def __init__(self, model: str="sam2.1_b.pt"):
        self.model = SAM(model)


    def segment(self, image: Image.Image, bboxes: Optional[list[int]], points: Optional[list[list[int]]]) -> Result:
        image_np = np.array(image)
        extra_args = {}
        if bboxes: extra_args["bboxes"] = bboxes
        if points: extra_args["points"] = points
        results = self.model(image_np, **extra_args)

        bounding_boxes = []
        segmentations = []

        for result in results:
            for box, segmentation in zip(result.boxes, result.masks):
                x_center, y_center, width, height = box.xywh[0]
                x_0, y_0 = int(x_center - width / 2), int(y_center - height / 2)
                x_1, y_1 = int(x_0 + width), int(y_0 + height)
                bounding_boxes.append(BoundingBox(x_0=x_0, y_0=y_0, x_1=x_1, y_1=y_1))
                segmentations.extend(Segmentation(points=[(int(x), int(y)) for x, y in seg]) for seg in segmentation.xy)

        return Result(bounding_boxes=bounding_boxes, segmentations=segmentations)
