from sqlalchemy.orm import Session

from app.models.project_note import (
    ProjectNote
)


def create_note(
    db: Session,
    user_id: int,
    project_id: int,
    note: str
):

    item = ProjectNote(
        user_id=user_id,
        project_id=project_id,
        note=note
    )

    db.add(item)

    db.commit()

    db.refresh(item)

    return item


def get_notes(
    db: Session,
    user_id: int,
    project_id: int
):

    return db.query(
        ProjectNote
    ).filter(
        ProjectNote.user_id == user_id,
        ProjectNote.project_id == project_id
    ).all()