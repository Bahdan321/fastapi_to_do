from fastapi import APIRouter
from view.home.homeRouter import home_route

main_api_router = APIRouter(prefix='/v1')

main_api_router.include_router(home_route)
