#include <SDL3/SDL.h>
#include <iostream>

int main() {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL_Init Error: " << SDL_GetError() << std::endl;
        return 1;
    }

    SDL_Window* window = SDL_CreateWindow("3D Cube - Two Dots", 800, 600, 0);
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

    // Define two 3D vertices
    float vertex1_x = -1.0f, vertex1_y = -1.0f, vertex1_z = -1.0f;
    float vertex2_x = 1.0f, vertex2_y = 1.0f, vertex2_z = -1.0f;

    bool running = true;
    SDL_Event e;
    while (running) {
        while (SDL_PollEvent(&e)) {
            if (e.type == SDL_EVENT_QUIT) {
                running = false;
            }
        }

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255); // Black background
        SDL_RenderClear(renderer);

        float distance = 2.0f;

        // Project and render vertex 1
        float scale1 = 200.0f / (vertex1_z + distance);
        float projected1_x = vertex1_x * scale1 + 400;
        float projected1_y = vertex1_y * scale1 + 300;
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255); // Red dot
        SDL_RenderPoint(renderer, (int)projected1_x, (int)projected1_y);

        // Project and render vertex 2
        float scale2 = 200.0f / (vertex2_z + distance);
        float projected2_x = vertex2_x * scale2 + 400;
        float projected2_y = vertex2_y * scale2 + 300;
        SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255); // Green dot
        SDL_RenderPoint(renderer, (int)projected2_x, (int)projected2_y);

        SDL_RenderPresent(renderer);
        SDL_Delay(16); // ~60 FPS
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
