from typing import List
import numpy as np
import cv2

from app.segmentators.segmentator import BoundingBox, Segmentation


def draw_bounding_boxes(image, bounding_boxes: List[BoundingBox]):
    for bbox in bounding_boxes:
        cv2.rectangle(image, (bbox.x_0, bbox.y_0), (bbox.x_1, bbox.y_1), (0, 255, 0), 2)  # Green bounding box
    return image

# Function to draw segmentations (polygons) on the image
def draw_segmentations(image, segmentations: List[Segmentation]):
    for seg in segmentations:
        segmentation_points = [tuple(p) for p in seg.points]
        if len(segmentation_points) > 1:
            cv2.polylines(image, [np.array(segmentation_points)], isClosed=True, color=(255, 0, 0), thickness=2)  # Blue polygon
    return image