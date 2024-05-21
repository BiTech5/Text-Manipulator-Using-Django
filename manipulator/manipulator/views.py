from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def manipulate_text(request):

    text = request.POST.get('text','default')
    toog_onoff=request.POST.get('switch','off')
    text=str(text)
    # print(text)
    head=''
    if toog_onoff=='off':
        return HttpResponse('Error')
    else:
        if toog_onoff=='count':
            head='Word And Character Count'
            total_wor=len(text.split())
            nbr=0
            for i in text:
                if i!=' ':
                    nbr+=1
                else:
                    pass
            text=f'Total word is {total_wor} and total character is {nbr}'
        elif toog_onoff=='uppercase':
            text_up=text.upper()
            head='Upper Case Text'
            text=text_up
        elif toog_onoff=='reverse':
            text=text[::-1]
            head='Reverse String'
        elif toog_onoff=='space':
            text=' '.join(text.split())
            head='Extra space remover'
        var_for_man={
            'heading':head,
            'para':text,
        }
        return render(request,'manupulation.html',var_for_man)

    
    