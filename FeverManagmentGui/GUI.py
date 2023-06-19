import os
import shutil
import driver_simple
import flet as ft


def delete():
    if os.path.exists('__pycache__'):
        print("Removing __pycache__")
        shutil.rmtree('__pycache__')
    if os.path.exists('compiled_krb'):
        print("Removing compiled_krb")
        shutil.rmtree('compiled_krb')


delete()

coughWillYesButton = ft.ElevatedButton("Yes")
coughWillNoButton = ft.ElevatedButton("No")
dyspneaYesButton = ft.ElevatedButton("Yes")
dyspneaNoButton = ft.ElevatedButton("No")
commonColdYesButton = ft.ElevatedButton("Yes")
commonColdNoButton = ft.ElevatedButton("No")
haemoptysisYesButton = ft.ElevatedButton("Yes")
haemoptysisNoButton = ft.ElevatedButton("No")
nightSweatYesButton = ft.ElevatedButton("Yes")
nightSweatNoButton = ft.ElevatedButton("No")
soreThroatYesButton = ft.ElevatedButton("Yes")
soreThroatNoButton = ft.ElevatedButton("No")
continueYesButton = ft.ElevatedButton("Continue")
continueNoButton = ft.ElevatedButton("No")

result = []


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def main(page: ft.Page):
    page.title = "PyKE Project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 500
    page.window_height = 500

    def refresh(e, question, yesButton, noButton):
        page.title = question
        page.clean()
        page.add(
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(question),
                            ft.Row([
                                yesButton,
                                noButton
                            ]),
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )
        page.update()

    def coughWill(e):
        refresh(e, "Do you have a cough will?", coughWillYesButton, coughWillNoButton)

    def dyspneaWithNoCoughWill(e):
        replace_line('bc_simple_rules_questions1.krb', 5, '        $coughYes = False' + '\n')
        refresh(e, "Do you have a dyspnea?", dyspneaYesButton, dyspneaNoButton)

    def dyspneaWithYesCoughWill(e):
        replace_line('bc_simple_rules_questions1.krb', 5, '        $coughYes = True' + '\n')
        refresh(e, "Do you have a dyspnea?", dyspneaYesButton, dyspneaNoButton)

    def commonColdWithNoDyspnea(e):
        replace_line('bc_simple_rules_questions1.krb', 6, '        $dyspneaYes = False' + '\n')
        refresh(e, "Do you have a common cold?", commonColdYesButton, commonColdNoButton)

    def commonColdWithYesDyspnea(e):
        replace_line('bc_simple_rules_questions1.krb', 6, '        $dyspneaYes = True' + '\n')
        refresh(e, "Do you have a common cold?", commonColdYesButton, commonColdNoButton)

    def haemoptysisWithNoCommonCold(e):
        replace_line('bc_simple_rules_questions1.krb', 13, '        $commonColdYes = False' + '\n')
        refresh(e, "Do you have a haemoptysis?", haemoptysisYesButton, haemoptysisNoButton)

    def haemoptysisWithYesCommonCold(e):
        replace_line('bc_simple_rules_questions1.krb', 13, '        $commonColdYes = True' + '\n')
        refresh(e, "Do you have a haemoptysis?", haemoptysisYesButton, haemoptysisNoButton)

    def nightSweatWithYesHaemoptysis(e):
        replace_line('bc_simple_rules_questions1.krb', 19, '        $haemoptysisYes = True' + '\n')
        refresh(e, "Do you have a night sweat?", nightSweatYesButton, nightSweatNoButton)

    def nightSweatWithNoHaemoptysis(e):
        replace_line('bc_simple_rules_questions1.krb', 19, '        $haemoptysisYes = False' + '\n')
        refresh(e, "Do you have a night sweat?", nightSweatYesButton, nightSweatNoButton)

    def soreThroatWithYesNightSweat(e):
        replace_line('bc_simple_rules_questions1.krb', 20, '        $nightSweatYes = True' + '\n')
        refresh(e, "Do you have a sore throat?", soreThroatYesButton, soreThroatNoButton)

    def soreThroatWithNoNightSweat(e):
        replace_line('bc_simple_rules_questions1.krb', 20, '        $nightSweatYes = False' + '\n')
        refresh(e, "Do you have a sore throat?", soreThroatYesButton, soreThroatNoButton)

    def wantToContinueWithYesSoreThroat(e):
        replace_line('bc_simple_rules_questions1.krb', 27, '        $soreThroatYes = True' + '\n')
        refresh(e, "Do you want to continue?", continueYesButton, continueNoButton)

    def wantToContinueWithNoSoreThroat(e):
        replace_line('bc_simple_rules_questions1.krb', 27, '        $soreThroatYes = False' + '\n')
        refresh(e, "Do you want to continue?", continueYesButton, continueNoButton)

    def ifRespiratorySymptoms(e):
        coughWill(e)

    def ifAbdominalPain(e):
        pass

    def ifUrinePain(e):
        pass

    def ifOther(e):
        pass

    def chooseCategory(e):
        page.clean()
        page.add(
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Choose what you are experiencing:"),
                            respiratorySymptomsButton,
                            abdominalPainButton,
                            urinePainButton,
                            otherButton,
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )
        delete()

    def wantToExit(e):
        page.clean()
        result = len(driver_simple.bc_test_questions1())
        for i in range(result):
            page.add(
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text(driver_simple.bc_test_questions1()[i]),
                            ],
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            )
        page.add(
            ft.Row([
                ft.Text("Thank you for using PyKE Project!", size=20),
                ft.Icon(ft.icons.WAVING_HAND_ROUNDED, size=50),
            ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    respiratorySymptomsButton = ft.ElevatedButton("Respiratory Symptoms", on_click=ifRespiratorySymptoms, data=True)
    abdominalPainButton = ft.FilledButton("Do you suffer from abdominal pain?", on_click=ifAbdominalPain, data=True)
    urinePainButton = ft.FilledButton("Do you suffer from urine pain?", on_click=ifUrinePain, data=True)
    otherButton = ft.FilledButton("other?", on_click=ifOther, data=True)

    coughWillYesButton.on_click = dyspneaWithYesCoughWill
    coughWillNoButton.on_click = dyspneaWithNoCoughWill
    dyspneaYesButton.on_click = commonColdWithYesDyspnea
    dyspneaNoButton.on_click = commonColdWithNoDyspnea
    commonColdYesButton.on_click = haemoptysisWithYesCommonCold
    commonColdNoButton.on_click = haemoptysisWithNoCommonCold
    haemoptysisYesButton.on_click = nightSweatWithYesHaemoptysis
    haemoptysisNoButton.on_click = nightSweatWithNoHaemoptysis
    nightSweatYesButton.on_click = soreThroatWithYesNightSweat
    nightSweatNoButton.on_click = soreThroatWithNoNightSweat
    soreThroatYesButton.on_click = wantToContinueWithYesSoreThroat
    soreThroatNoButton.on_click = wantToContinueWithNoSoreThroat
    continueYesButton.on_click = chooseCategory
    continueNoButton.on_click = wantToExit

    chooseCategory(None)


ft.app(target=main)
