def save_file(save_path, input_data):
    write_file = open(save_path, 'w', encoding='utf-8')

    for item_id in input_data:
        write_file.write(
            '[ID: {0}] {1}\n{2}\n\n----- ----- -----\n\n'.format(
                item_id,
                input_data[item_id]['Name_TC'],
                input_data[item_id]['Descript'],
            )
        )

    write_file.write('文件到此結束.')