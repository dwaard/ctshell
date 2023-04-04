import pandas as pd
import os
from envparse import env

class Context:

    def __init__(self):
        self.submissionPath = env("SUBMISSION_PATH")
        classroomFile = env("CLASSROOM_FILE")
        filepath = os.path.join(self.submissionPath, classroomFile)
        self.classroom = pd.read_csv(filepath, header=0)

    def clone(self, data):
        # Get the repository URL from the dataframe 
        repo_url = data['student_repository_url'].replace("https://github.com/", "git@github.com:") + ".git"
        repo_name = data['github_username']
        # Clone the repository into the destination directory
        cmd = f'git clone {repo_url} {self.submissionPath}/{repo_name}'
        print(cmd)
        os.system(cmd)

    def repoFolders(self):
        return [ f.name for f in os.scandir(self.submissionPath) if f.is_dir() ]

    def close(self):
        pass

