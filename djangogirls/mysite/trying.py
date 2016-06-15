def trying(request):
	levent = [{'bevent': bevent("Ozzy Osbourne","text", "http://127.0.0.1:8000/otherevent/1/", "1", "1","12.07.16", "7200-8200")},
	{'bevent': bevent("Iron Maiden", "text", "http://127.0.0.1:8000/otherevent/2/", "2", "1","25.06.16", "7200-9200")}]
	return render(request, "index.html", {'itemlist': levent})