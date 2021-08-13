import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RepoService {

  _URL = 'https://api.github.com/users/';
  token = '?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';

  constructor(public http: HttpClient) { }

  getRepo(searchTerm: string): Observable<any> {
    return this.http.get(this._URL + searchTerm + '/repos?' + this.token);
  }
}
