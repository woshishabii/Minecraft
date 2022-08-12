# -*- mode: python ; coding: utf-8 -*-
import time
import configparser
import subprocess

cp = configparser.ConfigParser()
cp.read('version')

def get_git_revision_hash() -> str:
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()

with open('commit_info', 'w') as commit_info:
    commit_info.write(get_git_revision_hash())

gen_name = f'{cp["DEFAULT"]["STAGE"]}-{cp["DEFAULT"]["VERSION"]}-{time.strftime("%Y%m%d%H%M%S", time.localtime())}-{get_git_revision_hash()}'

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/new/PycharmProjects/Minecraft'],
             binaries=[],
             datas=[
                    ('texture.png', '.'), 
                    ('pywintypes310.dll', '.'), 
                    ('version', '.'),
                    ('Minecraft.ttf', '.'),
                    ('connit_info', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name=gen_name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
