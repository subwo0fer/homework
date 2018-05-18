def get_free_land(area, l_w):
    if area[0] <= 0:
        raise ValueError('Не задана площадь участка')
    area_gryadki = l_w[0] * l_w[1]
    if area_gryadki > area[0] * 100:
        raise ValueError('Размер грядки больше размера участка')
    if area_gryadki <= 0:
        raise ValueError('Не задана площадь грядки')
    ostatok = area[0] * 100 % area_gryadki
    return ostatok
