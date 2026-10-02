import subprocess

commits = subprocess.check_output(['git', 'log', '--oneline', 'index.html']).decode('utf-8').splitlines()
for commit in commits:
    hash = commit.split(' ')[0]
    content = subprocess.check_output(['git', 'show', f'{hash}:index.html'])
    try:
        content_str = content.decode('utf-8')
        if 'ð' in content_str:
            print(f'Corrupted in: {commit}')
        else:
            print(f'Clean in: {commit}')
            break
    except Exception as e:
        print(f'Error reading {hash}')
