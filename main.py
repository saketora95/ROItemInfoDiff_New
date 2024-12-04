print('# 程式開始執行')

print('    - 程式正常執行時，視窗不會主動關閉。')
print('    - 若視窗突然消失，表示有地方執行失敗而導致程式自動關閉。\n')

import os
import sys
from lua_readable_transfer import lua_transfer
from item_writer import save_file
from diffrent_check import compare_dict

EXECUTE_PATH = os.path.abspath(os.path.dirname(sys.executable)) + '/'

def old_file_check():
    print('    # 舊版本確認 - 開始')
    print('        - 檢查檔案 [ NewItemInfo.lua ] ... ...')

    is_exist = os.path.exists(EXECUTE_PATH + 'NewItemInfo.lua')
    if is_exist:
        print('        - 檢查檔案 [ NewItemInfo.lua ] 結束，確認到了上版本的 lua 檔案；檢查上上版本檔案後，進行改名作業。')
        print('')
        print('        - 檢查檔案 [ OldItemInfo.lua ] ... ...')
        if os.path.exists(EXECUTE_PATH + 'OldItemInfo.lua'):
            print('        - 檢查檔案 [ OldItemInfo.lua ] 結束，確認到了上上版本的 lua 檔案，進行刪除作業。')
            print('')

            print('        - 刪除檔案 [ OldItemInfo.lua ] ... ...')
            os.remove(EXECUTE_PATH + 'OldItemInfo.lua')
            print('        - 刪除檔案 [ OldItemInfo.lua ] 結束。')
        else:
            print('        - 檢查檔案 [ OldItemInfo.lua ] 結束，沒有找到上上版本的 lua 檔案，略過刪除作業。')
        print('')

        print('        - 檔案改名 [ NewItemInfo.lua ] → [ OldItemInfo.lua ] ... ...')
        os.rename(EXECUTE_PATH + 'NewItemInfo.lua', 'OldItemInfo.lua')
        print('        - 檔案改名 [ NewItemInfo.lua ] → [ OldItemInfo.lua ] 結束。')
    else:
            print('        - 檢查檔案 [ NewItemInfo.lua ] 結束，沒有找到上版本的 lua 檔案，略過版本調整作業。')

    print('    # 舊版本確認 - 結束')
    return is_exist

def lub_to_lua(file_name):
    print('    # lub 轉換 lua - 開始')

    print('        - 轉換檔案 [ {}.lub ] → [ NewItemInfo.lua ] ... ...'.format(file_name))
    os.system('luadec.exe {}.lub > NewItemInfo.lua'.format(file_name))
    print('        - 轉換檔案 [ {}.lub ] → [ NewItemInfo.lua ] 結束。'.format(file_name))
    
    print('    # lub 轉換 lua - 結束')

def execute_different_check(encoding):
    print('    # 差異比對作業 - 開始')
    old_item_info_dict = lua_transfer(EXECUTE_PATH + 'OldItemInfo.lua', encoding)
    new_item_info_dict = lua_transfer(EXECUTE_PATH + 'NewItemInfo.lua', encoding)
    compare_dict(old_item_info_dict, new_item_info_dict, EXECUTE_PATH + 'CompareResult.txt', encoding)
    print('    # 差異比對作業 - 結束')

def build_readable_lua_info(encoding):
    print('    # 缺少上版本的 lua 檔案，僅進行文件可讀化作業。')
    print('    # 文件可讀化作業 - 開始')
    item_info_dict = lua_transfer(EXECUTE_PATH + 'NewItemInfo.lua', encoding)
    save_file(EXECUTE_PATH + 'NewItemInfo.txt', item_info_dict)
    print('    # 文件可讀化作業 - 結束')



print('# 決定模式')
print('    - [ 一般模式 ]: 直接按下 ENTER')
print('        - 目標為 twRO 的檔案時，')
print('          請使用這個選項。')
print('        - 過去未曾使用過的話會缺少比對用的檔案，')
print('          因此僅會建立轉換後的完整檔案供下次比對使用。')
print('    - [ 編碼模式 ]: 隨意輸入文字後，再按下 ENTER')
print('        - 若要使用特定編碼時，')
print('          請使用這個選項。\n')

if input('# 你想要怎麼進行？\n') == '':
    print('')
    print('# 一般模式 - 開始\n')
    exist_old_file = old_file_check()
    print('')
    lub_to_lua('iteminfo_new')
    print('')

    if exist_old_file:
        execute_different_check('utf-8')
        print('')
    else:
        build_readable_lua_info('utf-8')
        print('')

    print('# 一般模式 - 結束\n')
else:
    print('')
    print('# 你選擇了編碼模式')
    print('    - 接下來會需要你輸入兩筆資訊，')
    print('      若要採用預設值，')
    print('      直接按下 ENTER 即可。\n')

    specific_file_name = input('    # 請寫下「lub」檔案的的全名:\n        - 不包含附檔名，例如「iteminfo_new」。\n        - 預設值為 kRO 的「itemInfo_true」。\n')
    if specific_file_name == '':
        specific_file_name = 'itemInfo_true'
    print('    - 接受到你的輸入: \'{}\'\n'.format(specific_file_name))

    specific_encoding = input('    # 請寫下指定的編碼:\n        - 請以 Python 使用的代號為主。\n        - 預設值為 kRO 的「cp949」。\n')
    if specific_encoding == '':
        specific_encoding = 'cp949'
    print('    - 接受到你的輸入: \'{}\'\n'.format(specific_encoding))

    print('# 編碼模式 - 開始\n')
    exist_old_file = old_file_check()
    print('')
    lub_to_lua(specific_file_name)
    print('')

    if exist_old_file:
        execute_different_check(specific_encoding)
        print('')
    else:
        build_readable_lua_info(specific_encoding)
        print('')

    print('# 編碼模式 - 結束\n')
    
print('# 程式到此結束.\n')
os.system('pause')