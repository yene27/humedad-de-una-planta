Humedad = 0

def on_button_pressed_a():
    basic.show_string("H=")
    basic.show_number(Humedad)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global Humedad
    Humedad = pins.analog_read_pin(AnalogPin.P1)
    led.plot_bar_graph(Humedad, 1023)
    basic.pause(2000)
    if Humedad >= 340 and Humedad <= 680:
        basic.show_icon(IconNames.YES)
        basic.pause(1000)
        basic.show_string("NORMAL")
    elif Humedad < 340:
        basic.show_icon(IconNames.NO)
        basic.pause(1000)
        music.play_melody("G F G A G F E D ", 120)
        basic.show_string("BAJA")
    else:
        basic.show_icon(IconNames.CHESSBOARD)
        basic.pause(1000)
        basic.show_string("ALTA")
basic.forever(on_forever)
