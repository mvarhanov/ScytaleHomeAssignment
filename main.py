from extract_data import extract_base
from transform_data import transform_data

FILE_PATH = "json_data"


def main(file_path: str):
    try:
        if extract_base.extract_data(file_path):
            transform_data(file_path)
        print("Task is finish!")
    except Exception as e:
        print(f"Task failed with error: {e}")


if __name__ == "__main__":
    main(FILE_PATH)
