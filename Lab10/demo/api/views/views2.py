import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy

from api.serializers import CompanySerializer1, VacancySerializer2


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer1(companies, many=True)

        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        company = Company.objects.create(name=data.get('name'))
        return JsonResponse(company.to_json())

@csrf_exempt
def company_details(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == 'GET':
        return JsonResponse(company.to_json())
    if request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data.get('name')
        company.save()
        return JsonResponse(company.to_json())
    if request.method == 'DELETE':
        company.delete()
        return JsonResponse({"deleted": "True"})

@csrf_exempt
def vacancy_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer2(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = json.loads(request.body)
        vacancy = Vacancy.objects.create(
            name=data.get('name'),
            salary=data.get('salary'),
            company=Company.objects.get(id=data.get("company"))
        )
        return JsonResponse(vacancy.to_json())

@csrf_exempt
def vacancy_details(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    if request.method == 'PUT':
        data = json.loads(request.body)
        vacancy.name = data.get('name')
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    if request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({"deleted": "True"})


@csrf_exempt
def company_vacancies(request, company_id):
    vacancies = Vacancy.objects.all()
    result = []
    for v in vacancies:
        if v.company.id == company_id:
            result.append(v.to_json())
    return JsonResponse(result, safe=False)

@csrf_exempt
def top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')
    result = []
    countdown = 10
    for v in vacancies:
        if countdown == 0:
            break
        countdown -= 1
        result.append(v.to_json())

    return JsonResponse(result, safe=False)
