from app.segmentators.sam_2_segmentator import SAM2Segmentator
from app.segmentators.segmentator import Segmentator

segmentators_dict = {
    "sam2" : SAM2Segmentator
}

class SegmentatorFactory:
    def create_from(self, name: str, model: str) -> Segmentator:
        return segmentators_dict[name](model=model)