from lib.file_manager import FileManager
from lib.folder_manager import FolderManager

file_mgr = FileManager()
folder_mgr = FolderManager()

# Create new TEST folder for unittest
TEST_FOLDER_NAME = "TEST"
if folder_mgr.list_dir(remote_folder_path=TEST_FOLDER_NAME):
    folder_mgr.delete_folder(remote_folder_path=TEST_FOLDER_NAME)
folder_mgr.create_folder(remote_folder_path=TEST_FOLDER_NAME)


def test_create_new_file():
    assert file_mgr.create_file(f"{TEST_FOLDER_NAME}/test.txt", should_override=True) == True
    assert file_mgr.create_file(f"{TEST_FOLDER_NAME}/test.py", should_override=True) == True
    assert file_mgr.create_file(f"{TEST_FOLDER_NAME}/test", should_override=True) == True
    assert file_mgr.create_file(f"{TEST_FOLDER_NAME}/test", should_override=False) == False
    assert file_mgr.create_file(f"{TEST_FOLDER_NAME}/folder/test.xlsx", should_override=True) == True


def test_create_new_folder():
    assert folder_mgr.create_folder(remote_folder_path=f"{TEST_FOLDER_NAME}/folder/sub_folder") == True


def test_list_dir():
    result = folder_mgr.list_dir(remote_folder_path=TEST_FOLDER_NAME)
    assert result["numFiles"] == 3
    assert result["numDirs"] == 1
    result = folder_mgr.list_dir(remote_folder_path=f"{TEST_FOLDER_NAME}/folder")
    assert result["numFiles"] == 1
    assert result["numDirs"] == 1


def test_upload_file():
    assert file_mgr.upload_file(remote_file_path=f"{TEST_FOLDER_NAME}/folder/test.txt", local_file_path="./test_data/test.txt", should_override=True) == True


def test_get_file_info():
    info = file_mgr.get_file_info(remote_file_path=f"{TEST_FOLDER_NAME}/folder/test.txt")
    assert info["path"] == f"/{TEST_FOLDER_NAME}/folder/test.txt"
    assert info["type"] == "text"
    assert info["content"] == "Hello World!"


def test_update_file_content():
    assert file_mgr.update_file_content(remote_file_path=f"{TEST_FOLDER_NAME}/folder/test.txt", content="Updated!") == True
    info = file_mgr.get_file_info(remote_file_path=f"{TEST_FOLDER_NAME}/folder/test.txt")
    assert info["content"] == "Updated!"


def test_download_file():
    assert file_mgr.download_file(remote_file_path=f"{TEST_FOLDER_NAME}/folder/test.txt", local_file_path="./test_data/download.txt") == True


def test_zip_files():
    assert file_mgr.zip_files(
        remote_file_paths=[
            f"{TEST_FOLDER_NAME}/folder/test.txt",
            f"{TEST_FOLDER_NAME}/test.py",
            f"{TEST_FOLDER_NAME}/folder"
        ],
        local_file_path="./test_data/data.zip"
    ) == True


def test_delete_file():
    assert file_mgr.delete_file(remote_file_path=f"{TEST_FOLDER_NAME}/test") == True


def test_delete_folder():
    assert folder_mgr.delete_folder(remote_folder_path=f"{TEST_FOLDER_NAME}/folder") == True


def test_upload_folder():
    assert folder_mgr.upload_folder(remote_folder_path=f"{TEST_FOLDER_NAME}/my_folder", local_folder_path="./test_data/test_folder", should_override=True) == True
    assert folder_mgr.upload_folder(remote_folder_path=f"{TEST_FOLDER_NAME}/my_folder", local_folder_path="./test_data/test_folder", should_override=False) == False


def test_upload_large_files():
    assert folder_mgr.upload_folder(remote_folder_path=f"{TEST_FOLDER_NAME}/large_folder", local_folder_path="./test_data/large_files") == True
