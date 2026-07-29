import cv2
from pathlib import Path


def load_video(video_path: str):
    """
    Load a video using OpenCV and print its properties.
    """

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise FileNotFoundError(f"Could not open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    print("=" * 40)
    print("VIDEO INFORMATION")
    print("=" * 40)
    print(f"Path         : {video_path}")
    print(f"Resolution   : {width} x {height}")
    print(f"FPS          : {fps:.2f}")
    print(f"Total Frames : {total_frames}")
    print(f"Duration     : {duration:.2f} seconds")
    print("=" * 40)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("UBFC Video", frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parents[2]

    video_path = project_root / "dataset" / "UBFC-rPPG" / "subject1" / "vid.avi"

    load_video(str(video_path))