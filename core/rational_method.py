def rational_flow(c: float, i_mmh:float, area_ha:float) -> float:
    '''
    Calcula vazão pelo método racional
    Retorna Q em m³/s
    '''
    i_mms = i_mmh / 1000 / 3600 #Converte intensidade para m/s
    area_m2 = area_ha * 10000 #Converte área para m²
    q = c * i_mms * area_m2 # Calcula vazão

    return q