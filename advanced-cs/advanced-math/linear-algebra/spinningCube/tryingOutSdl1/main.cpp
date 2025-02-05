#include <SDL3/SDL.h>
#include <iostream>

int main() {
    // Initialize SDL3
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL_Init Error: " << SDL_GetError() << std::endl;
        return 1;
    }

    // Create SDL window with simplified SDL3 setup
    SDL_Window* window = SDL_CreateWindow(
        "3D Cube",                  
        800,                       
        600,                        
        0      
    );

    if (!window) {
        std::cerr << "SDL_CreateWindow Error: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }

    //// Create renderer for window
    //SDL_Renderer* renderer = SDL_CreateRenderer(window, NULL);
    //if (!renderer) {
    //    std::cerr << "SDL_CreateRenderer Error: " << SDL_GetError() << std::endl;
    //    SDL_DestroyWindow(window);
    //    SDL_Quit();
    //    return 1;
    //}

    //// Define one 3D vertex (x, y, z)
    //float vertex_x = -1.0f;
    //float vertex_y = -1.0f;
    //float vertex_z = -1.0f;

    //// Simple projection to 2D (ignoring Z for simplicity)
    //float projected_x = vertex_x * 200 + 400; 
    //float projected_y = vertex_y * 200 + 300;

    //// Main loop to render the vertex
    //bool running = true;
    //SDL_Event e;
    //while (running) {
    //    while (SDL_PollEvent(&e)) {
    //        if (e.type == SDL_EVENT_QUIT) {
    //            running = false;
    //        }
    //    }

    //    // Clear the screen with black color
    //    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255); // Black
    //    SDL_RenderClear(renderer);

    //    // Draw the vertex as a red dot (scaled to 2D)
    //    SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255); // Red color
    //    SDL_RenderPoint(renderer, (int)projected_x, (int)projected_y);

    //    // Present the rendered frame
    //    SDL_RenderPresent(renderer);

    //    // Delay to control frame rate (around 60 FPS)
    //    SDL_Delay(16);
    //}

    //// Clean up
    //SDL_DestroyRenderer(renderer);
    //SDL_DestroyWindow(window);
    //SDL_Quit();
    SDL_Delay(2000);

    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}



