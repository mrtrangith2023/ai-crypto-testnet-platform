from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.auth.dependencies import (
    get_current_user
)

from app.schemas.project_note import (
    ProjectNoteCreate,
    ProjectNoteResponse
)

from app.services.project_note_service import (
    create_note,
    get_notes
)

router = APIRouter(
    prefix="/projects",
    tags=["Project Notes"]
)


@router.post(
    "/{project_id}/notes",
    response_model=ProjectNoteResponse
)
def create_project_note(
    project_id: int,
    payload: ProjectNoteCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return create_note(
        db,
        int(current_user["sub"]),
        project_id,
        payload.note
    )


@router.get(
    "/{project_id}/notes",
    response_model=list[ProjectNoteResponse]
)
def get_project_notes(
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return get_notes(
        db,
        int(current_user["sub"]),
        project_id
    )