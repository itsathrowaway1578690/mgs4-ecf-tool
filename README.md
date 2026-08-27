# mgs4-ecf-tool
Tool to decrypt mgs4 ecf config files

To decrypt your own ECF files found in \steamapps\common\METAL GEAR SOLID 4\MGS4\config

Install python.

Backup files to a separate location.

Open CMD and go to the folder you have the backup files then run

python mgs4_tool.py decrypt FILENAME.ecf FILENAME.ini

Replacing FILENAME with the file you want to convert

After editing it, re-encrypt it with:

python mgs4_tool.py encrypt FILENAME.ini FILENAME_new.ecf

Replacing FILENAME with the file you want to convert

Then change FILENAME_new.ecf to the original file name and place it in the MGS4 config directory.

\steamapps\common\METAL GEAR SOLID 4\MGS4\config
