from django.shortcuts import render
from .models import Message

def board(request):
	messages = Message.objects.order_by('-date')
	if request.method == "POST":
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('board')
	else:
		form = MessageForm()
	return render(request, 'msgboard/board.html', {
		'messages': messages,
		'form': form,
	})
