import subprocess
import os
def git_push(repo_path=os.path.dirname(os.path.dirname(__file__)), remote='origin', branch='master'):
    try:
        # 切换到仓库目录
        subprocess.run(['git', '-C', repo_path, 'add', '.'], check=True)
        # 提交更改
        subprocess.run(['git', '-C', repo_path, 'commit', '-m', 'python爬虫获取新闻自动提交'], check=True)
        # 推送到远程仓库
        subprocess.run(['git', '-C', repo_path, 'push', remote, branch], check=True)
        print("成功推送到远程仓库。")
    except subprocess.CalledProcessError as e:
        print(f"推送过程中出现错误: {e}")
    except Exception as e:
        print(f"发生未知错误: {e}")

if __name__ == "__main__":
    # 替换为你的仓库路径
    git_push(os.path.dirname(os.path.dirname(__file__)))
    