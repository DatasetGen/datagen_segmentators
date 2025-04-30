# Datagen Segmentators

This project is a web-based tool for image segmentation using different segmentators. Users can upload an image, view segmentation results (bounding boxes and polygons), and interact with the visualized data through a user-friendly interface.

---

## Features

- Upload an image for segmentation.
- Visualize bounding boxes and segmentation polygons on separate canvases.
- Powered by FastAPI for the backend and a web-based frontend.
- Supports multiple segmentators (e.g., SAM, YOLO).

---

## Installation

### Prerequisites

- Docker installed on your system.

### Steps

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd datagen-segmentators
   ```

2. Build the Docker image:
   ```bash
   docker build -t datagen_segmentators .
   ```

3. Run the Docker container:
   ```bash
   docker run -p 8000:8000 datagen_segmentators
   ```

The application will be accessible at `http://localhost:8000`.

---

## Project Structure

- **main.py**: Entry point for the FastAPI server.
- **segmentators/**: Contains the logic for different segmentators.
- **static/**: Contains frontend files (HTML, CSS, JavaScript).
- **Dockerfile**: Configuration to containerize the application.
- **requirements.txt**: Python dependencies.

---

## Usage

1. Navigate to `http://localhost:8000` in your web browser.
2. Upload an image file via the provided form.
3. View the results:
   - Bounding boxes visualized on the "Bounding Boxes" canvas.
   - Segmentation polygons visualized on the "Segmentations" canvas.

---

## Development

### Running Locally

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

4. Open `http://127.0.0.1:8000` in your browser.

---

## Troubleshooting

### Error: `libGL.so.1: cannot open shared object file`

This occurs when OpenCV requires OpenGL libraries. Ensure the following dependencies are installed in the Docker image or on your system:
```bash
apt-get install -y libgl1 libglib2.0-0
```

Rebuild the Docker image if necessary.

---


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

---

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Ultralytics](https://ultralytics.com/) for segmentators.
- Open-source libraries and contributors.

---

## Contact

For any inquiries or support, please contact [your_email@example.com].

