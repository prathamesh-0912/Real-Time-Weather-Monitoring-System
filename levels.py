level_mapping = {
    '1000': 1, '925': 2, '850': 3, '700': 4, '600': 5, '500': 6, '400': 7,
    '300': 8, '250': 9, '200': 10, '150': 11, '100': 12
}

def getlevel(variable, level_type, selected_level, upper_level, lower_level, start_level, end_level):
    index_level, index_level1, index_level2, levels = 0, 0, 0, 0
    if level_type == 'single':
        index_level = level_mapping[selected_level]
        levels= selected_level
    elif level_type == 'multiple' and variable=="Geopotential Height":
        index_level1 = level_mapping[upper_level]
        index_level2 = level_mapping[lower_level]
        levels = f'{upper_level}-{lower_level}'
    elif level_type == 'multiple' and variable!="Tropospheric Temperature" and variable!="Tropospheric Thickness":
        index_level = slice(level_mapping[start_level], level_mapping[end_level]+1)
        levels = f'{start_level} to {end_level}'
    else:
        levels = f'1000-250'
        
    return index_level, index_level1, index_level2, levels