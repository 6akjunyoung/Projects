import os

def merge_gitignore_files(root_dir='.'):
    # Root 폴더의 .gitignore 파일 경로
    root_gitignore = os.path.join(root_dir, '.gitignore')
    
    # 통합할 내용 저장할 리스트
    merged_rules = []

    # 하위 폴더의 .gitignore 파일들 검색
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.git' in dirnames:
            dirnames.remove('.git')  # .git 폴더는 탐색에서 제외
        if '.gitignore' in filenames and dirpath != root_dir:
            # 각 폴더의 .gitignore 파일 경로
            gitignore_path = os.path.join(dirpath, '.gitignore')
            with open(gitignore_path, 'r') as f:
                rules = f.readlines()

            # 경로 추가해서 규칙 통합
            relative_path = os.path.relpath(dirpath, root_dir)
            relative_path = relative_path.replace('\\', '/')  # 경로 구분자를 '/'로 변경
            merged_rules.append(f"# Rules from {relative_path}/.gitignore\n")
            for rule in rules:
                rule = rule.strip()
                if rule and not rule.startswith('#'):  # 주석이나 빈 줄 제외
                    merged_rules.append(f"{relative_path}/{rule}\n")
            merged_rules.append("\n")

    # Root 폴더의 .gitignore에 추가
    with open(root_gitignore, 'a') as root_file:
        root_file.writelines(merged_rules)

    print(f"Successfully merged .gitignore files into {root_gitignore}")

if __name__ == "__main__":
    merge_gitignore_files()

