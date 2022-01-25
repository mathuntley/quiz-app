import PySimpleGUI as sg

qtitle = "Tytuł quizu"
questions = ["Export czy chmielowa?", "Butla czy pucha?"]
answers = [["Chmielowa", "Export", "Chuj to wie", "Nie wiem"], ["Butla", "Pucha", "Nie wiem", "Nie wiem ale na biało"]]
current_q = 1
image = f"img{current_q}.png"
answers_data = []

def calculate_result(a):
    if sum(a) < 10:
        return {"result": "Wynik", "desc": "Masz wielki penis", "img": "img_result1.png"}
    elif sum(a) < 25:
        return {"result": "Wynik", "desc": "Masz wielki penis", "img": "img_result1.png"}
    else:
        return {"result": "Wynik", "desc": "Masz wielki penis", "img": "img_result1.png"}


layout = [[sg.Text(qtitle, font="Arial 14", key="TITLE")],
          [sg.Text(f"{current_q} / {len(questions)}", key="QNUMDISPLAY")],
          [sg.Text(f"{questions[current_q - 1]}", font="Arial 22", key="QUESTION")],
          [sg.Image(image, key="IMAGE")],
          [sg.pin(sg.Radio(answers[current_q - 1][0], "ans", key="ANS1")), # https://stackoverflow.com/a/66660054
           sg.pin(sg.Radio(answers[current_q - 1][1], "ans", key="ANS2")),
           sg.pin(sg.Radio(answers[current_q - 1][2], "ans", key="ANS3")),
           sg.pin(sg.Radio(answers[current_q - 1][3], "ans", key="ANS4"))],
          [sg.Text("", visible=False, key="DESC")],
          [sg.pin(sg.Button("Wstecz", key="BACK")), sg.pin(sg.Button("Dalej", key="NEXT"))],
          [sg.pin(sg.Button("Zacznij od nowa", visible=False, key="RESTART"))]]

window = sg.Window("Quiz App", layout, finalize=True, element_justification="center")

while True:

    e, v = window.read()

    if e == sg.WINDOW_CLOSED:
        break

    elif e == "NEXT":
        if v["ANS1"] is True:
            print("Pressed 1")
            answers_data.append(5)
        elif v["ANS2"] is True:
            print("Pressed 2")
            answers_data.append(1)
        elif v["ANS3"] is True:
            print("Pressed 3")
            answers_data.append(15)
        elif v["ANS4"] is True:
            print("Pressed 4")
            answers_data.append(10)
        else:
            sg.PopupError("Nie zaznaczono odpowiedzi")
            continue
        current_q += 1
        if current_q > len(questions):
            r = calculate_result(answers_data)
            image = f"{r['img']}"
            window["QNUMDISPLAY"].update(visible=False)
            window["QUESTION"].update(r["result"])
            window["IMAGE"].update(image)
            window["ANS1"].update(visible=False)
            window["ANS2"].update(visible=False)
            window["ANS3"].update(visible=False)
            window["ANS4"].update(visible=False)
            window["DESC"].update(r["desc"], visible=True)
            window["BACK"].update(visible=False)
            window["NEXT"].update(visible=False)
            window["RESTART"].update(visible=True)
            print(answers_data)
        else:
            image = f"img{current_q}.png"
            window["QNUMDISPLAY"].update(f"{current_q} / {len(questions)}")
            window["QUESTION"].update(questions[current_q - 1])
            window["IMAGE"].update(image)
            window["ANS1"].update(text=answers[current_q - 1][0], value=False)
            window["ANS2"].update(text=answers[current_q - 1][1], value=False)
            window["ANS3"].update(text=answers[current_q - 1][2], value=False)
            window["ANS4"].update(text=answers[current_q - 1][3], value=False)

    elif e == "BACK":
        try:
            current_q -= 1
            window["QNUMDISPLAY"].update(f"{current_q} / {len(questions)}")
            window["QUESTION"].update(questions[current_q - 1])
            image = f"img{current_q}.png"
            window["IMAGE"].update(image)
            window["ANS1"].update(text=answers[current_q - 1][0], value=False)
            window["ANS2"].update(text=answers[current_q - 1][1], value=False)
            window["ANS3"].update(text=answers[current_q - 1][2], value=False)
            window["ANS4"].update(text=answers[current_q - 1][3], value=False)
            answers_data.pop(-1)
        except:
            sg.PopupError("Nie można się cofnąć!")

    elif e == "RESTART":
        current_q = 1
        image = f"img{current_q}.png"
        answers_data = []
        window["QNUMDISPLAY"].update(f"{current_q} / {len(questions)}", visible=True)
        window["QUESTION"].update(questions[current_q - 1])
        window["IMAGE"].update(image)
        window["ANS1"].update(text=answers[current_q - 1][0], visible=True, value=False)
        window["ANS2"].update(text=answers[current_q - 1][1], visible=True, value=False)
        window["ANS3"].update(text=answers[current_q - 1][2], visible=True, value=False)
        window["ANS4"].update(text=answers[current_q - 1][3], visible=True, value=False)
        window["BACK"].update(visible=True)
        window["NEXT"].update(visible=True)
        window["DESC"].update(visible=False)
        window["RESTART"].update(visible=False)

window.close()
