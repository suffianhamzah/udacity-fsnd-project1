Project 1: Interactive Website with Movie Trailers
==================================================

A website that contains movie trailers of several movies

# Installation:
First, either clone or download the project code from this repo:

#### Cloning using SSH or HTTPS
```
  $ git clone git@github.com:suffianhamzah/udacity-fsnd-project1.git
```

# Usage:
To open the website, run this command in your local copy of the repo:
```
  $ python entertainmentcenter.py
```

# Getting movies from MOVIEDB api:
This website also allows you to get different types of trailers, based on
the options you choose.

You would need to have a MovieDB api to use this feature.
You can obtain the API from the [MovieDB website](https://developers.themoviedb.org)
Then, you would need to set an evironment variable, 'MOVIEDB_API_TOKEN'.

To set the API as an environment variable, type:

#### macOS / linux:
```
  $ export MOVIEDB_API_TOKEN=<api_token> >> ~/.bashrc
```

#### Windows (Git Bash):
```
  $ export MOVIEDB_API_TOKEN=<api_token> >> C:\users\userName\git-home\.bash_profile
  # Referred from: https://stackoverflow.com/questions/34169721/set-an-environment-variable-in-git-bash
```

Options for movie trailers are:
* upcoming
* latest
* top_rated
* now_playing
* popular

To use this feature, type the command:
```
  $ python entertainmentcenter.py <trailer_type>
```

