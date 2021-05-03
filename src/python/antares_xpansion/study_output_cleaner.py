import os
from pathlib import Path


def remove_files_containing_str_from_dir(contains_str: str, dirpath: Path):
    for instance in os.listdir(dirpath):
        if contains_str in instance:
            os.remove(dirpath / instance)


class StudyOutputCleaner:

    @staticmethod
    def clean_antares_step(study_output: Path):
        remove_files_containing_str_from_dir('-1.mps', study_output)
        remove_files_containing_str_from_dir('criterion', study_output)
        remove_files_containing_str_from_dir('-1.txt', study_output)

    @staticmethod
    def clean_lpnamer_step(study_output: Path):
        remove_files_containing_str_from_dir('.mps', study_output)
        remove_files_containing_str_from_dir('constraints', study_output)
        remove_files_containing_str_from_dir('variables', study_output)
    @staticmethod
    def clean_benders_step(study_output: Path):
        remove_files_containing_str_from_dir('.mps', study_output / 'lp')
        remove_files_containing_str_from_dir('.lp', study_output / 'lp')

    @staticmethod
    def clean_study_update_step(study_output: Path):
        remove_files_containing_str_from_dir('area', study_output)
        remove_files_containing_str_from_dir('interco', study_output)
        remove_files_containing_str_from_dir('mps.txt', study_output)
