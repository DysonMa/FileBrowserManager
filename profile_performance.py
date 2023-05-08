from concurrent.futures import ThreadPoolExecutor
import time
from lib.folder_manager import FolderManager

class SequentialUploader:
    def __init__(self, folder_mgr: FolderManager, exec_times: int) -> None:
        self.folder_mgr = folder_mgr
        self.exec_times = exec_times

    def run(self) -> None:
        start = time.time()
        for iter_id in range(self.exec_times):
            self.folder_mgr.upload_folder(
                remote_folder_path=f"sequential/{str(iter_id+1)}",
                local_folder_path=TEST_FOLDER_PATH
            )
        end = time.time()
        print(f"Sequential elapse: {end - start}")


class ConcurrentUploader:
    def __init__(self, folder_mgr: FolderManager, exec_times: int) -> None:
        self.folder_mgr = folder_mgr
        self.exec_times = exec_times

    def upload_folder(self, remote_folder_path: str, local_folder_path: str):
        self.folder_mgr.upload_folder(remote_folder_path=remote_folder_path, local_folder_path=local_folder_path)

    def run(self) -> None:
        start = time.time()
        with ThreadPoolExecutor(max_workers=5) as executor:
            for iter_id in range(self.exec_times):
                executor.submit(self.upload_folder, remote_folder_path=f"concurrent/{str(iter_id+1)}", local_folder_path=TEST_FOLDER_PATH)
        end = time.time()
        print(f"Concurrent elapse: {end - start}")
        

if __name__ == "__main__":
    TEST_FOLDER_PATH = "./test_data/large_files"

    folder_mgr = FolderManager()
    exec_times = 10

    # Sequential
    seq_uploader = SequentialUploader(folder_mgr=folder_mgr, exec_times=exec_times)
    seq_uploader.run()

    # Concurrent
    concurr_uploader = ConcurrentUploader(folder_mgr=folder_mgr, exec_times=exec_times)
    concurr_uploader.run()


    