import base64
import io
from typing import Optional

from PIL import Image
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.segmentators.segmentator import Result
from app.segmentators.segmentator_factory import SegmentatorFactory
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specific allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
templates = Jinja2Templates(directory="templates")

class RequestBody(BaseModel):
    image : str
    segmentator: Optional[str] = "sam2"
    model : Optional[str] = "sam2_t.pt"
    bboxes: Optional[list[int]] = []
    points: Optional[list[list[int]]] = []

@app.post("/segment_image/")
async def segment(body: RequestBody) -> Result:
    image_data = base64.b64decode(body.image)
    image = Image.open(io.BytesIO(image_data))
    segmentator = SegmentatorFactory().create_from(name=body.segmentator, model=body.model)
    result = segmentator.segment(image, body.bboxes, body.points)
    return result

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

