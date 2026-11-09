import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import os
from .models import Task

def health_check(request):
    return HttpResponse("OK", status=200)

def index_view(request):
    index_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'index.html')
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            return HttpResponse(f.read())
    return HttpResponse("Index.html not found", status=404)

@csrf_exempt
def task_list_create(request):
    if request.method == 'GET':
        tasks = list(Task.objects.values('id', 'title', 'completed').order_by('id'))
        return JsonResponse(tasks, safe=False)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            if not title:
                return JsonResponse({'error': 'Title is required'}, status=400)
            task = Task.objects.create(title=title)
            return JsonResponse({'id': task.id, 'title': task.title, 'completed': task.completed}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def task_detail_update_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            task.completed = data.get('completed', task.completed)
            task.save()
            return JsonResponse({'id': task.id, 'title': task.title, 'completed': task.completed}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'success': True}, status=200)
        
    return JsonResponse({'error': 'Method not allowed'}, status=405)