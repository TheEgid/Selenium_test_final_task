import subprocess


if __name__ == '__main__':
    cmd_line = ['pytest', '--language=it', '--browser=chrome', 'test_product_page.py']
    subprocess.run(cmd_line)
