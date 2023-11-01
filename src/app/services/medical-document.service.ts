import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Observable, BehaviorSubject  } from 'rxjs';
import { ConstantsService } from './constants.service';

@Injectable({
  providedIn: 'root'
})
export class MedicalDocumentService {
  IHL_BASE_URL = this._constant.ihlBaseurl;
  private documentShareSubject = new BehaviorSubject<any[]>([]);
  readonly observedValue = this.documentShareSubject.asObservable();

  constructor(
    private httpClient: HttpClient,
    private _constant: ConstantsService
  ) { }

  public uploadFiles(data: any): Observable<any>{
    let headers = new HttpHeaders();
    return this.httpClient.post(`${this.IHL_BASE_URL}consult/upload_medical_document`, data, { reportProgress: true, observe: "events"});
  }

  public getAllMedicalFiles(data: any): Observable<any>{
    let headers = new HttpHeaders();
    return this.httpClient.post(`${this.IHL_BASE_URL}consult/view_user_medical_document`, data, {headers});
  }

  public deleteSeletectedFile(data: any): Observable<any>{
    let headers = new HttpHeaders();
    return this.httpClient.post(`${this.IHL_BASE_URL}consult/delete_medical_document`, data, {headers});
  }

  public selectedDocumentedId(data: any[]): void{
    this.documentShareSubject.next(Object.assign([], data));
  }

  public getselectedDocumentedId(): any{
    let data: any = "";
    this.observedValue.subscribe((val)=>{
      data =  val;
    });
    return data;
  }
}
