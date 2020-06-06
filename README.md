# Kemaru Game

##### Project created for assessment of subject "Introduction to python"

## Author:
```
PATIL Kunal
MSc, Artificial Intelligence
EPITA
```

## Resources used:
```
Editor: Pycharm Professional 2019.3
Framework: Flask
Languages used:
    Python 
    HTML
    CSS    
```

## Arborsence
```
Kemaru_Game-
    |- static
        |- <All images for creating game view>
    |- temp
        |- temp.json (temporary json file for saving current grid information)
    |- templates
        |- <All html files for creating game view>
    |- database
        |- init.py (initializing variables for grid patterns)
        |- urls.json (urls for fetching grids) 
        |- offline_grids.json (offline grids in case of network connectivity)
    |- app.py (Entry point of the application)
    |- controller.py (functions for processing the data)
    |- getBoard.py (creating grids for the game)
    |- requirements.txt (packages required for the project)
    |- sandbox.py (sandbox file for test code functionality)
    
```

## Usage and Features:
```
1. There are two levels available:
    - Normal (Default): 9x9 grid
    - Easy : 6x6 grid
2. Information available on home page:
    - Rules of the game
    - About the Game 
3. Depending on user's solution, comparing preloaded solution user will be redirected to:
    - user have correct solution:
        - redirect to page showing "you win"
        - option included "Go back to Home" for more puzzles
    - user tried to solve the grid:
        - if user wants to "give up"
            - option included "Give Up"
                - redirecting to page where user can see the solution
        - if user submitted wrong set
            - redirect to page showing "Sorry It's Wrong"
                - Here user will have options:
                    - See solution for given grid
                    - Go back to home page                     
```

## Future Enhancements:
```
1. Adding more complex levels
2. Generating border lines instead of color sets for inner patterns in grids
3. Creating as a service
``` 

## Github:
https://github.com/kunalpatz/Kemaru_Game.git
