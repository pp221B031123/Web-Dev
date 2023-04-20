import {Component, OnInit} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {Vacancy} from "../models";
import {VacancyService} from "../vacancy.service";
@Component({
  selector: 'app-company-vacancy',
  templateUrl: './company-vacancy.component.html',
  styleUrls: ['./company-vacancy.component.css']
})
export class CompanyVacancyComponent implements OnInit{
  vacancies: Vacancy[] = [];
  constructor(
    private route: ActivatedRoute,
    private vacancyService: VacancyService
  ) { }
  ngOnInit() {
    const routeParams = this.route.snapshot.paramMap;
    const companyIdFromRoute = Number(routeParams.get('companyId'));
    this.vacancyService.getVacancies(companyIdFromRoute).subscribe((data)=>{
      this.vacancies = data;
    })
  }
}
