#include <SDL3/SDL.h>
#include <cmath>

const int SCREEN_WIDTH = 800;
const int SCREEN_HEIGHT = 600;

struct Vec3 {
    float x, y, z;
};


Vec3 originalPoints[8] = {
    {-100, -100, -100}, {100, -100, -100}, {100, 100, -100}, {-100, 100, -100},
    {-100, -100, 100},  {100, -100, 100},  {100, 100, 100},  {-100, 100, 100}
};

Vec3 points[8];

int edges[12][2] = {
    {0, 1}, {1, 2}, {2, 3}, {3, 0},
    {4, 5}, {5, 6}, {6, 7}, {7, 4},
    {0, 4}, {1, 5}, {2, 6}, {3, 7}
};


void rotateCube(Vec3 points[], int numPoints, float angleX, float angleY) {
    float cosX = cos(angleX);
    float sinX = sin(angleX);
    float cosY = cos(angleY);
    float sinY = sin(angleY);

    //bugfix copy original points into points to avoid acceleration and warp
    for (int i = 0; i < 8; i++) {
        points[i] = originalPoints[i];
    }

    for (int i = 0; i < numPoints;i++)
    {
        Vec3 p = points[i];
        //rotate around x axis, x stays the same
        float newY = p.y * cosX - p.z * sinX;
        float newZ = p.y * sinX + p.z * cosX;

       //rotate around y axis, y stays the same 
        float newX = p.x * cosY + newZ * sinY;
        newZ = -p.x * sinY + newZ * cosY;


        points[i].x = newX;
        points[i].y = newY;
        points[i].z = newZ;
    }
    
    
}

SDL_Point project3D(Vec3 point) {
    float distance = 400;
    float scale = 200;      

    SDL_Point p;
    p.x = (int)(SCREEN_WIDTH / 2 + (point.x / (point.z + distance)) * scale);
    p.y = (int)(SCREEN_HEIGHT / 2 + (point.y / (point.z + distance)) * scale);
    return p;
}

void renderCube(SDL_Renderer* renderer, Vec3 points[], int edges[][2]) {
    SDL_Point projectedPoints[8];

    for (int i = 0; i < 8; i++) {
        projectedPoints[i] = project3D(points[i]);
    }

    for (int i = 0; i < 12; i++) {
        SDL_RenderLine(renderer,
            projectedPoints[edges[i][0]].x, projectedPoints[edges[i][0]].y,
            projectedPoints[edges[i][1]].x, projectedPoints[edges[i][1]].y);
    }
}

int main() {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window* window = SDL_CreateWindow("3D Rotating Cube", SCREEN_WIDTH, SCREEN_HEIGHT, 0);
    SDL_Renderer* renderer = SDL_CreateRenderer(window, NULL);

    bool running = true;
    SDL_Event event;
    float angleX = 0, angleY = 0;

    while (running) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_EVENT_QUIT) running = false;
        }
        angleX += 0.01f;
        angleY += 0.01f;
        rotateCube(points, 8, angleX, angleY);

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);

        renderCube(renderer, points, edges);
        SDL_RenderPresent(renderer);
        SDL_Delay(16);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    
    SDL_Quit();
    return 0;
}

