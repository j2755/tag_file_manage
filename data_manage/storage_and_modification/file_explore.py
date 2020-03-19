import os
import sys
import pathlib


class Navigator:
    def __init__(self, directory):
        self.home = directory


    def find_all_files_in_home(self):
        return [f for f in os.listdir(self.home) if os.path.isfile(os.path.join(self.home, f))]

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
        os.chdir(self.directory)
        directories = []
        for root, dirs, files in os.walk(".", topdown=True):
            if dirs == []:
                continue
            directories.append((root, dirs))
        return directories

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
    def find_mother_daughter_pairs_in_select_directory(self,directory):
        os.chdir(directory)        
        directories =[]
        for root, dirs, files in os.walk(".", topdown=True):
            if dirs == []:
                continue
            directories.append((root, dirs))
        return directories
