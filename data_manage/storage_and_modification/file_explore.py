import os
import sys
import pathlib


class Navigator:
    def __init__(self, directory):
        self.home = directory
        self.daughters = self.find_all_daughters_in_home()
        self.files = self.find_all_files_in_home()
        self.entries=self.daughters+self.files

    def find_all_daughters_in_home(self):
        return self.find_daughter_directories(self.home)

    def find_all_files_in_home(self):
        return self.find_files_in_select_directory(self.home)

    def find_all_files_of_type_in_home(self, filetype):
        files = []
        try:
            for f in os.listdir(self.home):
                if pathlib.Path(f).suffix == filetype:
                    files.append(f)
        except Exception as e:
            print(e)
        return files

    def find_mother_daughter_directories_from_home(self):
        return self.find_mother_daughter_pairs_in_select_directory(self.home)

    def find_daughter_directories(self, directory):
        return [f for f in os.listdir(directory) if not os.path.isfile(os.path.join(directory, f))]

    def find_files_in_select_directory(self, directory):
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    def find_all_files_of_type_in_select_directory(self, directory, file_type):
        files = []
        try:
            for f in os.listdir(directory):
                if pathlib.Path(f).suffix == filetype:
                    files.append(f)
        except Exception as e:
            print(e)
        return files

    def find_mother_daughter_pairs_in_select_directory(self, directory):
        os.chdir(directory)
        directories = []
        for root, dirs, files in os.walk(".", topdown=True):
            if dirs == []:
                continue
            directories.append((root, dirs))
        return directories
