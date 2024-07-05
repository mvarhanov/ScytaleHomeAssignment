import json
import os

import github.Repository
from github import Github
from utils import check_rate_limit

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')


class ExtractDataBase:
    def extract_data(self, file_path: str) -> bool:
        gh = Github(GITHUB_TOKEN)
        org_name = 'Scytale-exercise'
        try:
            org = gh.get_organization(org_name)
            repositories = org.get_repos()
        except Exception as e:
            repositories = None
            print(f"get_repos errors {e}")
        check_rate_limit()
        if not repositories:
            return False
        try:
            for repo in repositories:
                self.get_repo_data(repo=repo, file_path=file_path)
                check_rate_limit()
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        print("Extract data - success!")
        return True

    @staticmethod
    def get_repo_data(repo: github.Repository.Repository, file_path: str):
        repo_name = repo.name
        base_repo_data = {
            "full_name": repo.full_name,
            "id": repo.id,
            "name": repo_name,
            "owner_login": repo.owner.login
        }

        # Get pull requests for the repository
        data_list = []
        pull_requests = repo.get_pulls(state='all')
        check_rate_limit()
        for pull_request in pull_requests:
            updated_data = {
                "is_merged": pull_request.is_merged(),
                "updated_at": pull_request.updated_at.isoformat(),
            }
            new_data = {**base_repo_data, **updated_data}
            data_list.append(new_data)
            check_rate_limit()
        if not data_list:
            return

        # Save data to JSON file
        try:
            with open(f"{file_path}/{repo_name}_pull_requests.json", "w") as f:
                json.dump(data_list, f)
        except Exception as er:
            print(f"Write file error - {er}")


extract_base = ExtractDataBase()
