# -*- mode: python ; coding: utf-8 -*-
import time
import configparser
import pathlib

cp = configparser.ConfigParser()
cp.read('version')

def get_git_revision_hash() -> str:
    git_dir = pathlib.Path('.') / '.git'
    with (git_dir / 'HEAD').open('r') as head:
        ref = head.readline().split(' ')[-1].strip()
    with (git_dir / ref).open('r') as git_hash:
        return git_hash.readline().strip()[:7]

with open('commit_info', 'w') as commit_info:
    commit_info.write(get_git_revision_hash())

gen_name = f'{cp["DEFAULT"]["STAGE"]}-{cp["DEFAULT"]["VERSION"]}-{time.strftime("%Y%m%d%H%M%S", time.localtime())}-{get_git_revision_hash()}'

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/new/PycharmProjects/Minecraft'],
             binaries=[],
             datas=[
                    ('terrain.png', '.'), 
                    ('pywintypes310.dll', '.'), 
                    ('version', '.'),
                    ('Minecraft.ttf', '.'),
                    ('commit_info', '.')],
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
