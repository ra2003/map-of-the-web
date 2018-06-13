from django.shortcuts import render
from django.shortcuts import render_to_response
from motw.producing import processing
from motw.producing import Count
from bokeh.resources import CDN
from bokeh.embed import components

def test(request):
	query = request.GET.get('q','') 
	if query:
		fig = processing(query)
		total_number = Count(query)
		script1, div1 = components(fig[0], CDN)
		return render(request, 'test01.html', \
									{'script1': script1, 'div1': div1, \
									 'results': query, 'total_number': total_number})
	else:
		results = []
		return render_to_response('test01.html', {'results': results})
