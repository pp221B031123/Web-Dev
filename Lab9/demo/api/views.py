from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy


def company_list(request):
    companies = Company.objects.all()
    companies_json = [c.to_json() for c in companies]
    return JsonResponse(companies_json, safe=False)

def company_details(request, company_id):
    companies = Company.objects.all()
    for c in companies:
        if c.id == company_id:
            return JsonResponse(c.to_json())

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_details(request, vacancy_id):
    vacancies = Vacancy.objects.all()

    for v in vacancies:
        if v.id == vacancy_id:
            return JsonResponse(v.to_json())

def company_vacancies(request, company_id):
    vacancies = Vacancy.objects.all()
    result = []
    for v in vacancies:
        if v.company.id == company_id:
            result.append(v.to_json())
    return JsonResponse(result, safe=False)

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
