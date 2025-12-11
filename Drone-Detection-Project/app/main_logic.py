from .image_analyzer import ImageAnalyzer
from .video_analyzer import VideoAnalyzer
from pathlib import Path

def main():
    model_path = "models/last.pt"
    image_folder = Path("data/images")
    video_file = Path("data/videos/sample.mp4")
    output_folder = Path("data/Our_DataBase")

    # Analyze images
    analyzer = ImageAnalyzer(model_path=model_path)
    for img_path in image_folder.glob("*.jpg"):
        analyzer.analyze_image(img_path, output_folder=output_folder)

    # Analyze video
    video_analyzer = VideoAnalyzer(model_path=model_path)
    video_analyzer.detect_and_save_objects(video_file, output_folder=output_folder)

if __name__ == "__main__":
    main()
