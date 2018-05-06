def counter():
    from datetime import datetime, date, time, timedelta
    d = datetime.today()
    d2 = datetime(d.year + 1, 1, 1, 0, 0, 0)
    result = (d2 - d)
    result_chasi = result.seconds // 3600
    result_minuti = (result.seconds - result_chasi * 3600) // 60

    buf_dney = result.days % 100
    if buf_dney % 10 == 1 and buf_dney not in range(10, 21):
        vivod_den = 'день'
    elif buf_dney not in range(10, 21) and buf_dney % 10 in range(2, 5):
        vivod_den = 'дня'
    else:
        vivod_den = 'дней'

    if result_chasi % 10 == 1 and result_chasi % 10 != 11:
        vivod_chasi = 'час'
    elif result_chasi % 10 in range(2, 5) and result_chasi not in range(10, 21):
        vivod_chasi = 'часа'
    else:
        vivod_chasi = 'часов'

    if result_minuti % 10 == 1 and result_minuti % 10 != 11:
        vivod_minuti = 'минута'
    elif result_minuti % 10 in range(2, 5) and result_minuti not in range(10,21):
        vivod_minuti = 'минуты'
    else:
        vivod_minuti = 'минут'

    print(result.days, vivod_den, result_chasi, vivod_chasi, result_minuti, vivod_minuti)

counter()
