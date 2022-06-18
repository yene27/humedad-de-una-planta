let Humedad = 0
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showString("H=" + Humedad)
})
basic.forever(function () {
    Humedad = pins.analogReadPin(AnalogPin.P1)
    led.plotBarGraph(
    Humedad,
    1023
    )
    basic.pause(2000)
    if (Humedad >= 340 && Humedad <= 680) {
        basic.showString("N")
    } else if (Humedad < 340) {
        basic.showString("B")
    } else {
        basic.showString("A")
    }
})
