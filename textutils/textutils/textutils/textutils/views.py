from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
  #  return HttpResponse("Home")


def analyze(request):
   # get the text
    djtext = request.GET.get('text', 'default')
    # check checkbox value
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":

        punctuations = '''!:(){}[]-;,.'"\/<>?@#$%^&*-~_ '''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps == "on"):
      analyzed = ""
      for char in djtext:
        analyzed = analyzed + char.upper()

      params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}

      return render(request, 'analyze.html', params)

    elif(newlineremover == "on"):
       analyzed = ""
       for char in djtext:
        if char !="\n":

          analyzed= analyzed + char

       params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}

       return render(request, 'analyze.html', params)

    elif(extraspaceremover):
       analyzed = ""
       for index, char in enumerate (djtext):
        if djtext[index] ==" " and djtext[index+1]==" ":
          pass
        else:
          analyzed= analyzed + char

       params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed}

       return render(request, 'analyze.html', params)


    else:
        return HttpResponse("please select any one of the given options")

# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst")

# def newlineremove(request):
#     return HttpResponse("newlineremove")

# def spaceremover(request):
#     return HttpResponse("spaceremover")

# def charcounter(request):
#     return HttpResponse("charcounter")
