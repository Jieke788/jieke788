from github import Github

class PRSubmitter:
    def __init__(self, github_token, repo_name):
        self.github = Github(github_token)
        self.repo = self.github.get_repo(repo_name)

    def create_pull_request(self, branch_name, base_branch="main", title="Automated PR", body="Code refactor PR"):
        pr = self.repo.create_pull(
            title=title,
            body=body,
            base=base_branch,
            head=branch_name
        )
        return pr
