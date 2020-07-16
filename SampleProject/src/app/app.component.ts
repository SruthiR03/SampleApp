import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
//import { map } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  title = 'SampleProject';

  name = 'hi';
  email = 'john@gmail.com';

  constructor(private http: HttpClient) { }
  httpdata;
  ngOnInit() {
    this.http.get("http://127.0.0.1:5000/list").
    //pipe(map((response) => response.json())).
    subscribe((data) => this.displaydata(data));
}
displaydata(data) {this.httpdata = data;}

/*
 

  getTextFile() {
    // The Observable returned by get() is of type Observable<string>
    // because a text response was specified.
    // There's no need to pass a <string> type parameter to get().
    return this.http.get('http://127.0.0.1:5000/list')
      .pipe(
        tap( // Log the result or error
          data => this.log(filename, data),
          error => this.logError(filename, error)
        )
      );
  }
*/
}
