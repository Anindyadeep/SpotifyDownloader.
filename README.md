# SpotifyDownloader.
A Handy library for downloading songs, creating dataset. This library is aiming to provide these functionalities. 
  
  - A general library to download songs.
  - Open music based dataset library for research purposes. 
  - YouTube, Spotify integration so that users can easily add songs to playlist, create playlist from youtube songs. 

### Workflow and roadmap
These are the set of phases and it's corresponding potential features to be added.

**[Phase 0] : Experimentations**

  [x] Initialised the repo. 

  [x] Used the SpotiPy library, and Spotify API and getting successful responses. 

  [x] Started to create Object oriented style coding for the experimentations.
  
  [ ] Structure the code and organise it. 


**[Phase 1] : CI/CD**

  [ ] Initialise the docker CI/CD pipeline. 
  [ ] Start a workflow in which changes can be directly seen inside docker environment. 

**[Phase 2] : Feature adding.**

  [ ] Fast parallel multi song downloading. (using asyncio)
  [ ] Integrate YouTube API and Spotify API .
  [ ] Create a library that can connect to Drive and download that to Drive / Local 

**[Phase 3] : Website creation and CI/CD**

  [ ] Website creation using streamlit / Flask / Django.
  [ ] Deploy the website to heroku /  netlify. 
  [ ] Integrate a full custom CI/CD pipeline (using GitHub actions) that will integrate:
      - The Docker image to DockerHub
      - The PyPI library update.
      - Website backend update.

