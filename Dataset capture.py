import cv2
import os

def capture_and_save_images(roll_number):
    # Open the webcam
    cap = cv2.VideoCapture(0)  # 0 represents the default  
    camera (you can change it if you have multiple cameras)  
    output_folder = "dataset"
    # Folder where images will be saved 
    # Create a folder for the student if it doesn't exist
    student_folder = os.path.join(output_folder, roll_number)
    os.makedirs(student_folder, exist_ok=True)

    image_count = 0

    while image_count < 30:  # Capture 30 images
        ret, frame = cap.read()

        # Save the captured frame as an image
        image_filename = os.path.join(student_folder, 
        f"image_{image_count}.jpg")
        cv2.imwrite(image_filename, frame)

        print(f"Image {image_count + 1} captured and saved.")

        image_count += 1

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

    print(f"All {image_count} images captured and saved in 
    folder: {student_folder}")
