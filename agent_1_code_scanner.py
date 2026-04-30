import os
import re

class CodeScanner:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def scan_code(self):
        issues = []
        for root, dirs, files in os.walk(self.repo_path):
            for file in files:
                if file.endswith('.py'):  # 只扫描 Python 文件
                    with open(os.path.join(root, file), 'r') as f:
                        content = f.read()
                        issues += self.check_for_issues(content, file)
        return issues

    def check_for_issues(self, content, filename):
        issues = []
        if len(re.findall(r'def ', content)) > 5:  # 假设函数过多为重复问题
            issues.append(f'File {filename} has too many functions.')
        return issues
