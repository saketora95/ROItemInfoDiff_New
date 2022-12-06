print('# 程式開始執行\n')

import os
from lua_readable_transfer import lua_transfer
from item_writer import save_file
from diffrent_check import compare_dict

EXECUTE_PATH = os.path.abspath(os.path.dirname(__file__)) + '/'

# If exist old file but name is 'New', rename it
print('# 舊版本確認 - 開始')
diff_check = os.path.exists(EXECUTE_PATH + 'NewItemInfo.lua')
if diff_check:
    # If exist old file, remove if
    if os.path.exists(EXECUTE_PATH + 'OldItemInfo.lua'):
        os.remove(EXECUTE_PATH + 'OldItemInfo.lua')
        print('# - 發現上上版本文件, 將 [ OldItemInfo.lua ] 刪除')

    # Rename
    os.rename(EXECUTE_PATH + 'NewItemInfo.lua', 'OldItemInfo.lua')
    print('# - 發現上版本文件, 將 [ NewItemInfo.lua ] 文件名稱改為 [ OldItemInfo.lua ]')
print('# 舊版本確認 - 結束\n')

# Execute .bat file
print('# 將 [ iteminfo_new.lub ] 轉換為 [ NewItemInfo.lua ] - 開始')
os.system('luadec.exe iteminfo_new.lub > NewItemInfo.lua')
print('# 將 [ iteminfo_new.lub ] 轉換為 [ NewItemInfo.lua ] - 結束\n')

# Exist old file, diffrent check
if diff_check:
    print('# 將 [ OldItemInfo.lua ] 與 [ NewItemInfo.lua ] 進行比對 - 開始')
    old_item_info_dict = lua_transfer(EXECUTE_PATH + 'OldItemInfo.lua')
    new_item_info_dict = lua_transfer(EXECUTE_PATH + 'NewItemInfo.lua')
    compare_dict(old_item_info_dict, new_item_info_dict, EXECUTE_PATH + 'CompareResult.txt')
    print('# 將 [ OldItemInfo.lua ] 與 [ NewItemInfo.lua ] 進行比對 - 結束\n')

# Not exist old file, transfer lua file to readable format
else:
    print('# 將 [ NewItemInfo.lua ] 轉換為可讀版 [ NewItemInfo.txt ] - 開始')
    item_info_dict = lua_transfer(EXECUTE_PATH + 'NewItemInfo.lua')
    save_file(EXECUTE_PATH + 'NewItemInfo.txt', item_info_dict)
    print('# 將 [ NewItemInfo.lua ] 轉換為可讀版 [ NewItemInfo.txt ] - 結束\n')

print('# 程式到此結束.\n')
os.system('pause')