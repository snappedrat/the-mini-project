from django.shortcuts import render
from .form import TranslatorForm

# Create your views here.

# def translator(request, *args, **kwargs):
#     return render(request, "translator.html")


def translator(request):
    if request.method == "POST":
        form = TranslatorForm(request.POST)
        if form.is_valid():
            source_text = form.cleaned_data["source_text"]
            
            # Call your translation API here and store the result in a variable
            translated_text = source_text
            
            return render(request, "translator.html", {"form": form, "translated_text": translated_text})
    else:
        form = TranslatorForm()
        return render(request, "translator.html", {"form": form})