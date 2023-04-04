import pandas as pd
import os
from envparse import env
import subprocess

class Context:

    def __init__(self):
        self.submissionPath = env("SubmissionPath")
        classroomFile = env("ClassroomFile")
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

    def reset_template_project(self):
        pass

    def get_commit_count(self, repo):
        # Retrieve the number of commits from the cloned repository
        cmd = f'cd {self.submissionPath}/{repo} && git rev-list --count HEAD'
        commit_count = subprocess.check_output(cmd, shell=True).rstrip()
        return int(commit_count)

    def repoFolders(self):
        return [ f.name for f in os.scandir(self.submissionPath) if f.is_dir() ]

    def close(self):
        pass

