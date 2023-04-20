import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {HttpClient, HttpClientModule} from "@angular/common/http";
import { CompanyVacancyComponent } from './company-vacancy/company-vacancy.component';
import {RouterModule} from "@angular/router";

@NgModule({
  declarations: [
    AppComponent,
    CompanyVacancyComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    RouterModule.forRoot([
      {path: 'companies/:companyId', component: CompanyVacancyComponent},
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
