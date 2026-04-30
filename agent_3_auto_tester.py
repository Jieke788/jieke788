import subprocess

class AutoTester:
    def __init__(self, test_command="pytest"):
        self.test_command = test_command

    def run_tests(self):
        result = subprocess.run(self.test_command, shell=True, capture_output=True, text=True)
        return result.returncode == 0  # 返回 True 如果测试通过
