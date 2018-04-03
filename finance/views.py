from django.shortcuts import render

# Create your views here.

def company_article_list(request):
	return render(request, "finance/plotly.html", {})