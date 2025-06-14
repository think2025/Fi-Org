import os
import shutil
from datetime import datetime

# Define the source directory to organize (change this to your target folder)
SOURCE_DIR = r"C:\Users\L390\Desktop"

# Define file categories and their corresponding extensions
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".java"],
    "Executables": [".exe", ".msi", ".bat"],
    "Others": []
}

# Define the destination directory where categorized folders will be created
DEST_DIR = r"C:\Users\L390\Desktop\Orga"

# Log file to track operations
LOG_FILE = os.path.join(DEST_DIR, "file_organization_log.txt")

def setup_destination_folders():
    """Create destination folders if they don't exist."""
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
    for category in FILE_CATEGORIES:
        category_path = os.path.join(DEST_DIR, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

def log_operation(message):
    """Log operations to a file with a timestamp."""
    with open(LOG_FILE, "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {message}\n")

def get_file_category(file_extension):
    """Determine the category of a file based on its extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def organize_files():
    """Scan source directory, categorize files, and move them to respective folders."""
    file_count = 0
    moved_files = 0
    for filename in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, filename)
        if os.path.isfile(file_path) and filename != os.path.basename(__file__):
            file_count += 1
            file_extension = os.path.splitext(filename)[1]
            category = get_file_category(file_extension)
            destination_folder = os.path.join(DEST_DIR, category)
            destination_path = os.path.join(destination_folder, filename)
            base_name, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(destination_path):
                new_filename = f"{base_name}_{counter}{ext}"
                destination_path = os.path.join(destination_folder, new_filename)
                counter += 1
            try:
                shutil.move(file_path, destination_path)
                moved_files += 1
                log_operation(f"Moved '{filename}' to '{category}' folder")
            except Exception as e:
                log_operation(f"Error moving '{filename}': {str(e)}")
    log_operation(f"Processed {file_count} files, moved {moved_files} files successfully")

def main():
    """Main function to run the file organizer."""
    print("Starting file organization...")
    setup_destination_folders()  # Moved here to ensure directories exist before logging
    log_operation("File organization started")
    organize_files()
    print("File organization completed. Check the log file for details.")
    log_operation("File organization completed")

if __name__ == "__main__":
    main()
