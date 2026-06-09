from sqlalchemy.orm import Session

from app.models.project import Project

from app.schemas.project import (
    ProjectCreate
)

def create_project(
    db: Session,
    payload: ProjectCreate
):

    project = Project(
        name=payload.name,
        ecosystem=payload.ecosystem,
        funding=payload.funding,
        status=payload.status,
        website=payload.website,
        twitter=payload.twitter
    )

    db.add(project)

    db.commit()

    db.refresh(project)

    return project


def get_projects(
    db: Session
):

    return db.query(
        Project
    ).all()