import base64
import io
from typing import Optional

from PIL import Image
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from segmentators.sam_2_segmentator import SAM2Segmentator
from segmentators.segmentator import Result
from segmentators.segmentator_factory import SegmentatorFactory

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class RequestBody(BaseModel):
    image : str
    segmentator: Optional[str] = "sam2"
    model : Optional[str]

@app.post("/segment_image/")
async def segment(body: RequestBody) -> Result:
    image_data = base64.b64decode(body.image)
    image = Image.open(io.BytesIO(image_data))
    segmentator = SegmentatorFactory().create_from(name=body.segmentator)
    result = segmentator.segment(image)
    return result

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

