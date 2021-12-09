import os
import os.path
import filecmp
from shutil import copyfile
from time import sleep


class FileTransferManager:
    def __init__(self, ) -> None:
        """"""
        self.repo_path = os.getcwd()
        self.file_list = []

    def read_files(self):
        """Parse the files.txt list. """
        with open("files.txt") as f:
            for i, fullpath in enumerate(f.readlines()):
                if not os.path.exists(fullpath.strip()):
                    print("File not found: %s" % fullpath.strip())
                    print("Omitting this file")
                    continue
                self.file_list.append(fullpath.strip())

    def commit_files(self):
        """Update current folder with modified files"""
        for fullpath in self.file_list:
            fname = os.path.split(fullpath)[-1]
            if (os.path.exists(fname) and not filecmp.cmp(fname, fullpath)) :
                copyfile(fullpath, fname)
            if not os.path.exists(fname):
                copyfile(fullpath, fname)
                os.system("git add %s"%fname)
        os.system("git commit -am 'update'")
        os.system("git push")

    def start(self, minimum_push_lag=20):
        """Initiate manager"""
        update_count = 0
        while True:
            banner = '-'*36+'Update #%d' % update_count + '-'*36
            self.read_files()
            print(banner)
            self.commit_files()
            print('-'*len(banner))
            sleep(minimum_push_lag)
            update_count += 1


path_to_repo = r"C:\Users\Administrator\Desktop\current\FileTransfer"
manager = FileTransferManager()
manager.start(240)
