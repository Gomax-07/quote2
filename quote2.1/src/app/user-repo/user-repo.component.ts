import { Component, OnInit } from '@angular/core';
import { RepoService } from './../repo.service';
import { Repos } from './../module/repos';

@Component({
  selector: 'app-user-repo',
  templateUrl: './user-repo.component.html',
  styleUrls: ['./user-repo.component.css']
})
export class UserRepoComponent implements OnInit {

  repo: Repos[] = [];

  constructor(public repoService: RepoService) { }

  getRepo(searchTerm: string) {
    this.repoService.getRepo(searchTerm).subscribe(data => {
      this.repo = data;
      console.log(this.repo)
    })
  }

  ngOnInit(): void {
    this.getRepo('Gomax-07');
  }

}
