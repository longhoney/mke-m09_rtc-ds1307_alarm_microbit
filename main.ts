// Gắn pin vào thì mạch sẽ tự lưu thời gian về đếm thời gian ngay cả khi không có nguồn
// 
// Mỗi lần reset sẽ cài đặt lại thời gian, ngày tháng theo thông tin này
ds3231.setTime_byChoose(30, ds3231.Month.Apr, 2026, 11, 14)
ds3231.setAlarm_byChoose(11, 15, ds3231.Alarm.OneTime)
basic.showLeds(`
    . . # . .
    . . # . .
    # # # . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    # . . . #
    . # . # .
    . . # . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . . # . .
    . . # . .
    . . # # #
    . . . . .
    . . . . .
    `)
basic.forever(function () {
    lcd.displayText(ds3231.getCalendar(), 1, 1)
    lcd.displayText(ds3231.getTime(), 1, 2)
    // Khi alarm xảy ra, microbit sẽ làm gì
    if (ds3231.checkAlarm()) {
        lcd.clearScreen()
        lcd.displayText("Alarm at 11:15", 1, 1)
        lcd.displayText(ds3231.getTime(), 1, 2)
        music.play(music.builtinPlayableSoundEffect(soundExpression.happy), music.PlaybackMode.UntilDone)
    }
    basic.pause(1000)
})
