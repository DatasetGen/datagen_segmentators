from segmentators.sam_2_segmentator import SAM2Segmentator
from segmentators.segmentator import Segmentator

segmentators_dict = {
    "sam2" : SAM2Segmentator
}

class SegmentatorFactory:
    def create_from(self, name: str) -> Segmentator:
        return segmentators_dict[name]()