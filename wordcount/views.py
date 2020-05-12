from django.shortcuts import render

# Create your views here.

# request가 들어오면 'home.html'을 리턴해라
# render(요청/응답, 템플릿 이름, 딕셔너리 자료형)
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dict = {}

    for word in words:

        # increase
        if word in word_dict:
            word_dict[word] += 1

        # add to dict
        else:
            word_dict[word] = 1


    return render(request, 'result.html', {'full':text, 'total':len(words), 'dict' : word_dict.items()})
    