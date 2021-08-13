import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent implements OnInit {

  searchTerm!: string;
  @Output() searchEmiter = new EventEmitter<any>();

  constructor() { }

  newUser() {
    this.searchEmiter.emit(this.searchTerm);

  }

  ngOnInit(): void {
  }

}
