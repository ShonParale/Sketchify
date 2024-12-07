import cv2
import time
import webbrowser

def sketch_image(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load the image. Please check the path.")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Use Canny Edge Detection
    edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)

    # Save the result
    cv2.imwrite(output_path, edges)
    print(f"Image sketched successfully! Saved as: {output_path}")

def sketch_video(video_path, output_path):
    # Load the video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open the video. Please check the path.")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 output
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height), isColor=False)

    print("\nProcessing video. This may take time depending on video length and quality.")
    print("Progress:")

    # Process the video frame-by-frame
    for frame_count in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break  # End of video

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian Blur to reduce noise
        blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        # Apply Canny Edge Detection
        edges_frame = cv2.Canny(blurred_frame, threshold1=50, threshold2=150)

        # Write the processed frame to the output video
        out.write(edges_frame)

        # Display progress percentage
        progress = int((frame_count / total_frames) * 100)
        print(f"\rLoading... {progress}% complete", end='')

    # Release the video objects
    cap.release()
    out.release()
    print("\nVideo sketched successfully! Saved as: {}".format(output_path))

def main():
    print("Please ensure that you provide the correct file path, file name, and file extension.")
    print("If any of these are incorrect, the program will not work as expected.\n")
    
    print("Note: Longer video files, higher resolution, or higher quality will take more time to process.\n")

    while True:
        print("Choose an option:")
        print("1: Sketch an Image")
        print("2: Sketch a Video")
        print("3: Exit")
        print("4: Info")
        choice = input("Enter 1, 2, 3, or 4: ")

        if choice == '1':
            image_path = input("Enter the image file path (e.g., image.jpg): ")
            output_path = input("Enter the output image file path (e.g., sketched_image.jpg): ")
            sketch_image(image_path, output_path)
        elif choice == '2':
            video_path = input("Enter the video file path (e.g., video.mp4): ")
            output_path = input("Enter the output video file path (e.g., sketched_video.mp4): ")
            sketch_video(video_path, output_path)
        elif choice == '3':
            print("Exiting the program.")
            break
        elif choice == '4':
            print("Opening the GitHub page...")
            webbrowser.open("https://github.com/ShonParale/Sketchify")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
