#include <SDL3/SDL.h>
#include <iostream>

int main() {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL_Init Error: " << SDL_GetError() << std::endl;
        return 1;
    }

    SDL_Window* window = SDL_CreateWindow("3D Cube", 800, 600, 0);
    if (!window) {
        std::cerr << "SDL_CreateWindow Error: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }

    SDL_Renderer* renderer = SDL_CreateRenderer(window, nullptr);
    if (!renderer) {
        std::cerr << "SDL_CreateRenderer Error: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }
    /*return the vertices in form (x,y,z) clockwise direction*/
    float cube[8][3] = {
        { -1, -1, -1 },//front bottom left vertex
        { -1,  1, -1 },//front top left vertex 
        {  1,  1, -1 },//front top right vertex
        {  1, -1, -1 },//front bottom right vertex
        { -1, -1,  1 },//back bottom left vertex
        { -1,  1,  1 },//back top left vertex
        {  1,  1,  1 },//back top right vertex
        {  1, -1,  1 },//back bottom right vertex
    };

    int edges[12][2] = {
        {0, 1}, {1, 2}, {2, 3}, {3, 0},
        {4, 5}, {5, 6}, {6, 7}, {7, 4},
        {0, 4}, {1, 5}, {2, 6}, {3, 7}
    };

    bool running = true;
    
    float distance = 2.0f;

    SDL_Event e;
    while (running) {
        while (SDL_PollEvent(&e)) {
            if (e.type == SDL_EVENT_QUIT) {
                running = false;
            }
        }

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255); 
        SDL_RenderClear(renderer);
        
      
        /*for (int i = 0; i < 8; i++) {
            float x = cube[i][0];
            float y = cube[i][1];
            float z = cube[i][2];
            float scale1 = 200.0f / (z + distance);
            float projected1_x = x * scale1 + 400;
            float projected1_y = y * scale1 + 300;
            SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
            SDL_RenderPoint(renderer, (int)projected1_x, (int)projected1_y);
            std::cout << projected1_x << " x " << projected1_x << " y" << std::endl;
            
        }*/

        /*project x,y,z, x' = x/z * d and y' = x/y * d */
        auto project = [&](float x, float y, float z, int& screenX, int& screenY) {
            float scale = 200.0f / (z + distance);
            screenX = (int)(x * scale + 400);
            screenY = (int)(y * scale + 300);
            };
        
        for (int i = 0; i < 12; i++) {
            int vertex1 = edges[i][0];
            int vertex2 = edges[i][1];
            int x0, y0, x1, y1;
            project(cube[vertex1][0], cube[vertex1][1], cube[vertex1][2], x0, y0);
            project(cube[vertex2][0], cube[vertex2][1], cube[vertex2][2], x1, y1);
            SDL_SetRenderDrawColor(renderer, 0, 0, 255, 255);
            SDL_RenderLine(renderer, x0, y0, x1, y1);
        }
        SDL_RenderPresent(renderer);
        SDL_Delay(16); // ~60 FPS
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
