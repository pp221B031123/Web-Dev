import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {Company, Vacancy} from "./models";
import {HttpClient, HttpClientModule} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class VacancyService {

  BASE_URL = 'http://127.0.0.1:8000'
  constructor(private client: HttpClient) { }

  getVacancies(companyId: number): Observable<Vacancy[]> {
    return this.client.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${companyId}/vacancies`);
  }
}
