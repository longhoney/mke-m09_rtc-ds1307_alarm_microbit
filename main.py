# Gắn pin vào thì mạch sẽ tự lưu thời gian về đếm thời gian ngay cả khi không có nguồn
# 
# Mỗi lần reset sẽ cài đặt lại thời gian, ngày tháng theo thông tin này
ds3231.setTime_byChoose(30, ds3231.Month.APR, 2026, 11, 14)
ds3231.setAlarm_byChoose(11, 15, ds3231.Alarm.ONE_TIME)
basic.show_leds("""
    . . # . .
    . . # . .
    # # # . .
    . . . . .
    . . . . .
    """)
basic.show_leds("""
    # . . . #
    . # . # .
    . . # . .
    . . . . .
    . . . . .
    """)
basic.show_leds("""
    . . # . .
    . . # . .
    . . # # #
    . . . . .
    . . . . .
    """)

def on_forever():
    lcd.display_text(ds3231.get_calendar(), 1, 1)
    lcd.display_text(ds3231.get_time(), 1, 2)
    # Khi alarm xảy ra, microbit sẽ làm gì
    if ds3231.check_alarm():
        lcd.clear_screen()
        lcd.display_text("Alarm at 11:15", 1, 1)
        lcd.display_text(ds3231.get_time(), 1, 2)
        music.play(music.builtin_playable_sound_effect(soundExpression.happy),
            music.PlaybackMode.UNTIL_DONE)
    # Báo thức vào giờ đó mỗi ngày
    if ds3231.setAlarm_byCommands("SA-11:16", ds3231.Alarm.ONE_TIME):
        lcd.clear_screen()
        lcd.display_text("Alarm at 11:16", 1, 1)
        lcd.display_text(ds3231.get_time(), 1, 2)
        music.play(music.builtin_playable_sound_effect(soundExpression.slide),
            music.PlaybackMode.UNTIL_DONE)
    basic.pause(1000)
basic.forever(on_forever)
