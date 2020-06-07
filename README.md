# GitHub Profile Scraper

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [GitHub Profile Scraper](#github-profile-scraper)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Usage](#usage)
      - [User details](#user-details)
      - [Repository details](#repository-details)
      - [Commit details](#commit-details)
  - [Goals](#goals)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
## About the Project

- A simple tool to fetch user details of a GitHub profile.
- It is built on top of [GitHub API v3](https://developer.github.com/v3/).
- Data is stored and manipulated in form of JSON.
- The data which can be categorized in 3 classed

  - **User Data** that contains user stats such 'Name', 'Location', 'Email', 'Followers' etc.
    Also stores a **Repository** list of the user.

  - **Repo Data** is used to collect data about a particular repository, such as 'number of forks', 'number of commits' etc.
  - **Commit Data** can be used to scrape commit history and 'Sha' values along with commit message.


![](docs/giphy.gif)

## Getting Started

### Installation
To get started clone this repository first
```bash
git clone https://github.com/AvikantSrivastava/GitHub-Profile-Scraper.git
```

### Usage

#### User details
To get user details import ```user.py``` in your project.
```python
from user import User

user = User('Username here')
```
```python
# to get user stats and save in json format
UserData = user.get_user_stats() 
print(UserData)

# to get repository list and save in json format
RepoData = user.get_repo_list()
print(RepoData)
```




#### Repository details
To get repository details import ```repo.py``` in your project.
```python
from repo import Repo

repo = Repo('Repository name here')
```

```python
# to get repository  stats and save it in json format
RepoData = repo.get_repo_stats() 
print(RepoData)

# to get a list of all the commit IDs and save them in json format
CommitIDs = repo.get_sha_values()
print(CommitIDs)

### Repository details
To get repository details import ```repo.py``` in your project.
```




#### Commit details
To get Commit details import ```commit.py``` in your project.
```python
from commit import Commit

project = Commit('Username here', 'Repository name here','commit ID here')
```

```python
# to get Commit stats and save them in json format
CommitData = project.get_commit_stats() 
print(CommitData)
```
## Goals
- Make a Driver program [CLI/GUI].
- Add more formats such as CSV and YML.


## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your Changes 
   ```bash
    git commit -m 'Add some AmazingFeature'
    ```
6. Push to the Branch 
```bash
    git push origin feature/AmazingFeature
```
7. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Avikant Srivastava - [@Aestheticell](https://twitter.com/Aestheticell) -
asdavikant@gmail.com

Project Link: [https://github.com/AvikantSrivastava/GitHub-Profile-Scraper](https://github.com/AvikantSrivastava/GitHub-Profile-Scraper)
