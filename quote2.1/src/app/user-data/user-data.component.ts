import { Component, OnInit } from '@angular/core';
import { GitServiceService } from './../git-service.service';
import { Users } from './../module/users';

@Component({
  selector: 'app-user-data',
  templateUrl: './user-data.component.html',
  styleUrls: ['./user-data.component.css']
})
export class UserDataComponent implements OnInit {

  user: Users[] = [];

  constructor(private gitServiceService: GitServiceService) { }

  getUser(searchTerm: string) {
    this.gitServiceService.searchUser(searchTerm).then((success) => {
      this.user = this.gitServiceService.user;
      console.log(this.user);

    }, (error) => {
      console.log(error);
    }
    )
  }

  ngOnInit(): void {
    this.getUser('Gomax-07');
  }

}
