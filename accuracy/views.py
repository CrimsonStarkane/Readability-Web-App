from django.shortcuts import render
from django import forms

from .formulas import *

class CalculateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), label="", min_length=150, max_length=3000)


formulas = {
    "Flesch-Kincaid Grade": flesch_kin,
    "SMOG Grade": smog,
    "Coleman-Liau Index": coleman,
    "Automated Readability Index": auto,
    "Linsear Write": linsear,
    "Rix": rix
}

names = list(formulas.keys())

def index(request):
    return render(request, "accuracy/index.html", {
        "formulas": names
    })


def prompt(request, formula):
    if request.method == "POST":
        form = CalculateForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            result = formulas[formula](text)
            
            if result != None:
                return render(request, "accuracy/prompt.html", {
                    "formula": formula,
                    "form": form,
                    "result": result,
                    "confirmation": "Text has been successfully analyzed! Scroll down to the bottom to see the result."
                })

            return render(request, "accuracy/prompt.html", {
                "formula": formula,
                "form": form,
                "message": "For this formula, your text must have a minimum of 100 words"
            })
        else:
            return render(request, "accuracy/prompt.html", {
                "formula": formula,
                "form": form
            })

    return render(request, "accuracy/prompt.html", {
        "formula": formula,
        "form": CalculateForm()
    })

def texts(request, formula):
    return render(request, "accuracy/texts.html", {
        "formula": formula
    })

def contacts(request):
    return render(request, "accuracy/contacts.html")