from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.auth.dependencies import (
    get_current_user
)

from app.schemas.project import (
    ProjectCreate,
    ProjectResponse
)
from app.services.project_service import (
    create_project,
    get_projects,
    search_projects,
    get_project_by_id,
    get_project_stats
)
from fastapi import Query

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.post(
    "/",
    response_model=ProjectResponse
)
def create_new_project(
    payload: ProjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return create_project(
        db,
        payload
    )


@router.get(
    "/",
    response_model=list[ProjectResponse]
)
def list_projects(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return get_projects(
        db
    )

@router.get(
    "/search",
    response_model=list[ProjectResponse]
)
def search_project(
    name: str | None = None,
    ecosystem: str | None = None,
    status: str | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):
    return search_projects(
        db,
        name,
        ecosystem,
        status
    )

@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
def project_detail(
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):
    return get_project_by_id(
        db,
        project_id
    )

@router.get(
    "/stats/overview"
)
def stats(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):
    return get_project_stats(
        db
    )