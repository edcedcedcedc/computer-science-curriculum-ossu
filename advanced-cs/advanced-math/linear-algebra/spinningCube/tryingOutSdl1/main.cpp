#include <SDL3/SDL.h>
#include <iostream>
#include <cmath>

struct Vertex {
    float x, y;
};

// Square points (centered at (0,0))
Vertex square[4] = {
    {-50, -50}, {50, -50}, {50, 50}, {-50, 50}
};

SDL_Window* window;
SDL_Renderer* renderer;
bool running = true;

// Function to apply transformations (identity for now)
void transform(Vertex& v) {
    // Identity transformation (just return the same point)
    float newX = v.x;
    float newY = v.y;
    v.x = newX;
    v.y = newY;
}

void drawSquare() {
    Vertex transformed[4];

    // Apply transformation
    for (int i = 0; i < 4; i++) {
        transformed[i] = square[i];
        transform(transformed[i]);
    }

    // Offset for screen center
    int cx = 400, cy = 300;

    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
    for (int i = 0; i < 4; i++) {
        int next = (i + 1) % 4;
        SDL_RenderLine(renderer,
            transformed[i].x + cx, transformed[i].y + cy,
            transformed[next].x + cx, transformed[next].y + cy);
    }
}

int main() {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL_Init Error: " << SDL_GetError() << std::endl;
        return 1;
    }

    window = SDL_CreateWindow("2D Transformations", 800, 600, 0);
    if (!window) {
        std::cerr << "SDL_CreateWindow Error: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }

    renderer = SDL_CreateRenderer(window, nullptr);
    if (!renderer) {
        std::cerr << "SDL_CreateRenderer Error: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    SDL_Event e;
    while (running) {
        while (SDL_PollEvent(&e)) {
            if (e.type == SDL_EVENT_QUIT) {
                running = false;
            }
        }

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        drawSquare();

        SDL_RenderPresent(renderer);
        SDL_Delay(16); // ~60 FPS
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}

