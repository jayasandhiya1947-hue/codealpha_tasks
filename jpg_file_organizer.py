import os
import shutil

def organize_jpg_files():

    print("=" * 60)
    print("              JPG FILE ORGANIZER")
    print("=" * 60)

    # Folder where the program is running
    source_folder = os.getcwd()

    # Folder where JPG files will be moved
    destination_folder = os.path.join(source_folder, "JPG_Images")

    # Create destination folder if it does not exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    moved_files = 0

    print("\nScanning folder...")
    print("Source folder:", source_folder)

    # Check all files in the source folder
    for file_name in os.listdir(source_folder):

        # Check whether the file is JPG or JPEG
        if file_name.lower().endswith((".jpg", ".jpeg")):

            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)

            # Make sure it is a file
            if os.path.isfile(source_path):

                # Move the image
                shutil.move(source_path, destination_path)

                print(f"Moved: {file_name}")
                moved_files += 1

    print("\n" + "-" * 60)

    if moved_files > 0:
        print(f"✅ Successfully organized {moved_files} JPG file(s).")
        print("📁 Files moved to:", destination_folder)
    else:
        print("⚠️ No JPG or JPEG files were found.")

    print("-" * 60)
    print("JPG File Organizer completed!")
    print("=" * 60)


organize_jpg_files()