from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.exceptions import ValidationError,status
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)

@api_view(['POST'])
def post(request):
	employee = EmployeeSerializer(data=request.data)
	if Employee.objects.filter(**request.data).exists():
		raise ValidationError("employee already in exists")
	if employee.is_valid():
		employee.save()
		return Response(employee.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_items(request):
	
	
	if request.query_params:
		items = Employee.objects.filter(**request.query_params.dict())
	else:
		items = Employee.objects.all()

	if items:
		serializer = EmployeeSerializer(items, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_items(request, pk):
	item = Employee.objects.get(pk=pk)
	data = EmployeeSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(Employee, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)
