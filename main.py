from agent_1_code_scanner import CodeScanner
from agent_2_restructure_suggester import CodeRestructureSuggester
from agent_3_auto_tester import AutoTester
from agent_4_pr_submitter import PRSubmitter

def main():
    repo_path = "/path/to/your/repo"
    openai_key = "your-openai-api-key"
    github_token = "your-github-token"
    repo_name = "username/repo-name"

    scanner = CodeScanner(repo_path)
    issues = scanner.scan_code()
    if issues:
        print(f"Issues found: {issues}")
    else:
        print("No issues found.")

    suggester = CodeRestructureSuggester(openai_key)
    code_snippet = "def example(): pass"
    suggestion = suggester.generate_suggestions(code_snippet)
    print(f"Suggestions: {suggestion}")

    tester = AutoTester()
    test_result = tester.run_tests()
    if test_result:
        print("Tests passed!")
    else:
        print("Tests failed!")

    pr_submitter = PRSubmitter(github_token, repo_name)
    pr = pr_submitter.create_pull_request("feature-branch")
    print(f"Pull request created: {pr.html_url}")

if __name__ == "__main__":
    main()
