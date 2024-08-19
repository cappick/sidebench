
import os

def file_list_md():
    """
    This function returns a list of markdown files in the current directory.
    """
    md_files = os.listdir('gzh_md')
    md_files = [file for file in md_files if file.endswith('.md')]
    md_files.sort()
    bg_files = os.listdir('gzh_bg')
    bg_files = [file for file in bg_files if file.endswith('.md')]
    bg_files.sort()
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write('## MD\n\n')
        for file in md_files:
            rel_path = f'gzh_md/{file}'
            f.write('- [{}]({})\n'.format(file.replace('.md', ''), rel_path))
        f.write('\n## BG\n\n')
        for file in bg_files:
            rel_path = f'gzh_bg/{file}'
            f.write('- [{}]({})\n'.format(file.replace('.md', ''), rel_path))
    with open('_sidebar.md', 'w', encoding='utf-8') as f:
        f.write('- MD\n\n')
        for file in md_files:
            rel_path = f'gzh_md/{file}'
            f.write('   - [{}]({})\n'.format(file.replace('.md', ''), rel_path))
        f.write('\n- BG\n\n')
        for file in bg_files:
            rel_path = f'gzh_bg/{file}'
            f.write('   - [{}]({})\n'.format(file.replace('.md', ''), rel_path))


if __name__ == '__main__':
    file_list_md()